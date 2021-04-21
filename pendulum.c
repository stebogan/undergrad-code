// Simulate simple oscillating pendulum (limit of small theta)
# include <stdio.h>
#include <math.h>

double f(double x)
{
    double a;
    a = -9.8*0.5*sin(x); //length = 2
    return a;
}

int main(void)
{
    double theta=0.5, omega=0, t, dt=0.000001;
    int frame = 0;

    for (t=0; 1; t+=dt)
    {
        if (omega > 0)
        {
            printf("Half period w/ interp: %.15f | No interp: %.15f\n", t-(omega/f(theta)), t);

            break;
        }
        if (frame % 2000 == 0)
        {

            printf("l 0.0 0.0 %e %e\n", 2*sin(theta), -2*cos(theta));
            printf("t -0.5 0.5\n");
            printf("t=%f\n", t);
            printf("F\n");

        }
      frame++;
      theta = theta+omega*dt;
      omega = omega+f(theta)*dt;
    }
}
