# include <stdio.h>
# include <math.h>

//global variables

double mu=1, k=100, m=0.2, Lo=2, Ls, dt=0.00001, E, T;
int N=30, n=2;

// Position Update
double pos_update(double x[], double y[], double vx[], double vy[])
{
    int i;

    for (i=1; i<N; i++)
  {
    x[i]=x[i]+vx[i]*dt/2;
    y[i]=y[i]+vy[i]*dt/2;
  }
}

//Velocity Update
double vel_update(double x[], double y[], double vx[], double vy[])
{
    double Lleft, Lright;
    int i;

    for (i=1; i<N; i++)
  {
    Lleft=hypot((x[i]-x[i-1]),(y[i]-y[i-1]));
    Lright=hypot((x[i]-x[i+1]),(y[i]-y[i+1]));
    vx[i]=vx[i]+(((k*(Lleft-Lo/N)*((x[i-1]-x[i])/Lleft))+(k*(Lright-Lo/N)*((x[i+1]-x[i])/Lright)))/m)*dt;
    vy[i]=vy[i]+(((k*(Lleft-Lo/N)*((y[i-1]-y[i])/Lleft))+(k*(Lright-Lo/N)*((y[i+1]-y[i])/Lright)))/m)*dt;
  }
}

int main()
{
  double x[N+1], y[N+1], vx[N+1], vy[N+1], t;
  int i, frame=0;
  double Ls=Lo*1.5;

  for (i=0; i<N+1; i++)
  {

      x[i]=i*Ls/N;
      y[i]=0.35*sin(n*M_PI*x[i]/Ls);
      vx[i]=0;
      vy[i]=0;
   }

  for (t=0; 1; t+=dt)
  {
    //Period Update
    if (vy[N/(2*n)] > 0)
    {
      T = 2*t;
      printf("!One half period elapsed: period is %e\n", T);
      break;
    }
    
    if (frame % 2000 == 0)
    {
      for (i=0; i<N+1; i++)
      {
        printf("c %f %f 0.001\n", x[i],y[i]);

        if (i != N)
        {
        printf("l %f %f %f %f\n", x[i],y[i],x[i+1],y[i+1]);
        }
      }
      printf("t 1 1.5\n");
      printf("E=%.15f\n", E);
      printf("F\n");
    }
    frame++;
    pos_update(x, y, vx, vy);
    vel_update(x, y, vx, vy);
    pos_update(x, y, vx, vy);
    E=0;
    for (i=0;i<N+1; i++)
    {
      E+=(0.5*m*pow(vy[i], 2)) + (0.5*k*pow(Ls-Lo, 2));
    }
  }
}
