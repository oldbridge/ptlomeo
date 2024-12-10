import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta

# Constantes pro visualizatione
gradus_tempus = 500
fps = 30  # Gradus per secundo pro animatione
signa_zodiac = [
    '\u2648 Aries', '\u2649 Taurus', '\u264A Gemini',
    '\u264B Cancer', '\u264C Leo', '\u264D Virgo',
    '\u264E Libra', '\u264F Scorpio', '\u2650 Sagittarius',
    '\u2651 Capricorn', '\u2652 Aquarius', '\u2653 Pisces'
]

# Datum fundamentale et epocha
initium_datum = datetime(2024, 1, 1)
datum_epocha = datetime(2000, 1, 1)  # J2000.0 pro positionibus referentibus

# Parametri orbitali (radius_deferentis, radius_epicycli, periodus_deferentis, periodus_epicycli, angulus_initialis)
# Anguli initiales sunt valores approximati pro 2024-01-01
data_planetarum = {
    "Luna": (2, 0.3, 27, 13, 125.08, 'violet'),  # Proxima Terrae
    "Mercurius": (3, 0.5, 88, 22, 252.25, 'yellow'),
    "Venus": (4, 0.4, 225, 50, 181.98, 'green'),
    "Sol": (12, 0, 365, 1e6, 280.46, 'orange'),  # Nullus epicyclus pro Sole
    "Mars": (6, 1.0, 687, 140, 355.45, 'red'),
    "Iuppiter": (8, 1.5, 4333, 398, 34.35, 'blue'),
    "Saturnus": (10, 2.0, 10759, 746, 49.24, 'indigo')  # Longissime a Terra
}

# Convertere gradus in radians
def gradus_in_radianos(gradus):
    return np.radians(gradus)

# Definire modelum Ptolemaicum pro planetis
class Planeta:
    def __init__(self, nomen, radius_deferentis, radius_epicycli, periodus_deferentis, periodus_epicycli, angulus_initialis, color):
        self.nomen = nomen
        self.radius_deferentis = radius_deferentis
        self.radius_epicycli = radius_epicycli
        self.periodus_deferentis = periodus_deferentis
        self.periodus_epicycli = periodus_epicycli
        self.angulus_initialis = gradus_in_radianos(angulus_initialis)
        self.color = color

    def positio(self, t):
        # Computare tempus elapsum ab epocha
        dies_ab_epocha = (initium_datum - datum_epocha).days + t
        theta_deferentis = self.angulus_initialis + 2 * np.pi * dies_ab_epocha / self.periodus_deferentis
        theta_epicycli = 2 * np.pi * dies_ab_epocha / self.periodus_epicycli
        x_deferentis = self.radius_deferentis * np.cos(theta_deferentis)
        y_deferentis = self.radius_deferentis * np.sin(theta_deferentis)
        x_epicycli = self.radius_epicycli * np.cos(theta_epicycli)
        y_epicycli = self.radius_epicycli * np.sin(theta_epicycli)
        x = x_deferentis + x_epicycli
        y = y_deferentis + y_epicycli
        return x, y, (x_deferentis, y_deferentis)

# Initiare omnes corpora caelestia in ordine Ptolemaico
planetae = [
    Planeta(nomen, *parametri)
    for nomen, parametri in data_planetarum.items()
]

# Preparatio ad animationem
figura, axis = plt.subplots(figsize=(8, 8))
axis.set_xlim(-14, 14)
axis.set_ylim(-14, 14)
axis.set_aspect('equal')
axis.axis('off')

# Zodiacus circulus
circulus_zodiacus = plt.Circle((0, 0), 13, color='black', fill=False)
axis.add_artist(circulus_zodiacus)
for i, signum in enumerate(signa_zodiac):
    angulus = i * 2 * np.pi / 12
    axis.text(13.5 * np.cos(angulus), 13.5 * np.sin(angulus), f"{signum}", ha='center', va='center')

# Traces et circuli
traces = []
puncta = []
lineae = []
deferentes = []
epicycli = []

# Initiare pro singulis planetis
for planeta in planetae:
    trace, = axis.plot([], [], lw=0.5)
    punctum, = axis.plot([], [], 'o', label=planeta.nomen, color=planeta.color)
    linea, = axis.plot([], [], color='gray', linestyle='dashed')
    deferens = plt.Circle((0, 0), planeta.radius_deferentis, color='gray', fill=False, linestyle='dotted')
    epicyclus = plt.Circle((0, 0), planeta.radius_epicycli, color='gray', fill=False, linestyle='dotted')
    axis.add_artist(deferens)
    axis.add_artist(epicyclus)
    traces.append(trace)
    puncta.append(punctum)
    lineae.append(linea)
    deferentes.append(deferens)
    epicycli.append(epicyclus)

# Annontatio temporis
textus_datum = axis.text(-13, 13, '', fontsize=12, ha='left')

# Functio pro update animatione
def renovatio(fra):
    t = int(fra)  # Certum est fra esse integer
    datum_currente = initium_datum + timedelta(days=t)
    textus_datum.set_text(datum_currente.strftime("Datum: %Y-%m-%d"))
    
    for i, planeta in enumerate(planetae):
        x, y, (x_deferentis, y_deferentis) = planeta.positio(t)
        traces[i].set_data(x, y)
        puncta[i].set_data(x, y)
        lineae[i].set_data([0, x], [0, y])
        deferentes[i].center = (0, 0)
        epicycli[i].center = (x_deferentis, y_deferentis)
    return traces + puncta + lineae + deferentes + epicycli + [textus_datum]

# Animatio
ani = FuncAnimation(figura, renovatio, frames=np.arange(0, gradus_tempus), interval=1000/fps, blit=False)

# Monstrare animationem
plt.legend(loc='upper right')
plt.show()
