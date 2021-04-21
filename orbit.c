# include <stdio.h>
# include <math.h>

int main(void)
{
    double t, x= 1, y= 0, r=pow(pow((x+0.5),2)+pow((y+0.5),2),0.5), GM=4*M_PI*M_PI, v_x= 0, v_y= sqrt(GM/r), dt=0.0001;
    //orbital velocity in terms of x, y only
    double E;
    int frame = 0;

    for (t=0; 1; t+=dt)
    {
        if (frame%40 == 0)
        {
            printf("c -0.5 -0.5 0.1\n");
            printf("c %f %f 0.05\n", x, y);
            printf("t 1 2\n");
            printf("t=%f\n", t);
            printf("t 0 3\n");
            printf("E=%.15f\n", E);
            printf("F\n");
        }
        frame++;
        x=x+v_x*dt/2;
        y=y+v_y*dt/2;
        r=pow(pow((x+0.5),2)+pow((y+0.5),2),0.5);
        v_x=v_x-((GM*(x+0.5))/pow(r,3+0.00001))*dt;
        v_y=v_y-((GM*(y+0.5))/pow(r,3+0.00001))*dt;
        x=x+v_x*dt/2;
        y=y+v_y*dt/2;
        r=pow(pow((x+0.5),2)+pow((y+0.5),2),0.5);
        E=0.5*(pow(v_x,2)+pow(v_y,2))-(GM/r);
    }
}
