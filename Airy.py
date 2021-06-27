from scipy.special import gamma
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *
from manim import *

y0 = [1 / (3 ** (2 / 3) * gamma(2 / 3)), -1 / (3 ** (1 / 3) * gamma(1 / 3))]


def model(t, y):
    return [t * y[1], y[0]]


sol = solve_ivp(model, [-15, 5], y0, t_eval=np.linspace(-15, 5, 400))

coords = np.array([sol.t, sol.y[1], np.zeros(len(sol.t))]).T

class OdeSol(Scene):
    def construct(self):
        axis = Axes(
            x_range=[-15,1,1],
            y_range=[-1,1,.2]
        )
        points = []

        for i in range(len(sol.t)):
            points.append(axis.coords_to_point(coords[i][0], coords[i][1]))

        path=VMobject(color=GREEN)
        path.set_points_smoothly(points)
        self.play(Write(axis, run_time=2))
        self.play(Create(path,run_time=5))



# fig, ax = plt.subplots()
# ax.plot(t, result[:, 0], label = 'R0=0')
# ax.plot(t, result[:,0], label = 'R0=0.3')
# ax.plot(t, result[:,0], label = 'R0=1')
# ax.legend()
# ax.set_xlabel('t')
# ax.set_ylabel('Rp')
# plt.show()
