from scipy.integrate import solve_ivp
from manim import *

y0 = [0.5,0.7]


def model(t,y):
    return [y[0]-y[0]*y[1]-0.4*y[0], -y[1]+y[0]*y[1]-0.2*y[1]]


t0 = 0
tmax = 12
sol = solve_ivp(model, [t0, tmax], y0, t_eval=np.linspace(t0, tmax, 100))

pointsprey = np.array([sol.t, sol.y[0], np.zeros(len(sol.t))]).T
pointspred = np.array([sol.t, sol.y[1], np.zeros(len(sol.t))]).T

class OdeSol(Scene):
    def construct(self):
        axis = Axes(
            x_range=[t0,tmax,1],
            y_range=[0,3,.25],
            axis_config={
                "graph_origin": ORIGIN
            }
        )


        predpoints = []
        preypoints = []
        predval = VGroup()
        preyval = VGroup()
        for i in range(len(sol.t)):
            predpoints.append(axis.coords_to_point(pointspred[i][0], pointspred[i][1]))
            preypoints.append(axis.coords_to_point(pointsprey[i][0], pointsprey[i][1]))
            predval.add(MathTex(f"Predators = {int(round(pointspred[i][1]*100,0))}", color=RED).shift(2*UP+4*RIGHT))
            preyval.add(MathTex(f"Prey = {int(round(pointsprey[i][1]*100,0))}", color=BLUE).shift(UP+4*RIGHT))

        preypath = VMobject(color=BLUE)
        preypath.set_points_smoothly(preypoints)

        predpath = VMobject(color=RED)
        predpath.set_points_smoothly(predpoints)

        self.play(Write(axis, run_time=2))
        self.play(Create(predpath, run_time=20, rate_func=linear),
                    Create(preypath, run_time=20, rate_func=linear),
                    ShowSubmobjectsOneByOne(predval, run_time=20, rate_func=linear),
                    ShowSubmobjectsOneByOne(preyval, run_time=20, rate_func=linear)
                  )
        self.wait(5)