// Simulate binary star system with arbitrary initial conditions
# include <stdio.h>
# include <math.h>

int main(void)
{
  double x_1=-1, y_1=0, x_2=1, y_2=0;
  //variables
  double r = pow(pow((x_1-x_2),2)+pow(y_1-y_2,2),0.5), dt = 0.0001, GM_1 = 4*M_PI*M_PI,
              GM_2=4*M_PI*M_PI;
  //dynamical variables
  double t, v_1_x=0, v_1_y=2.5, v_2_x=0, v_2_y=-2.5;
  //initial frame
  int frame = 0;

  for (t = 0; 1; t+=dt)
  {
    if (frame % 40 == 0)
    {
      printf("c %f %f 0.1\n", x_1, y_1);
      printf("c %f %f 0.1\n", x_2, y_2);
      printf("F\n");
    }
    frame++;
    //postion update
    x_1=x_1+v_1_x*dt/2;
    y_1=y_1+v_1_y*dt/2;

    x_2=x_2+v_2_x*dt/2;
    y_2=y_2+v_2_y*dt/2;
    //radius update
    r = pow(pow((x_1-x_2),2)+pow(y_1-y_2,2),0.5);
    //velocity update
    v_1_x=v_1_x-((x_1-x_2)*GM_1/pow(r,3))*dt;
    v_1_y=v_1_y-((y_1-y_2)*GM_1/pow(r,3))*dt;

    v_2_x=v_2_x-((x_2-x_1)*GM_2/pow(r,3))*dt;
    v_2_y=v_2_y-((y_2-y_1)*GM_2/pow(r,3))*dt;
    //second postion update
    x_1=x_1+v_1_x*dt/2;
    y_1=y_1+v_1_y*dt/2;

    x_2=x_2+v_2_x*dt/2;
    y_2=y_2+v_2_y*dt/2;
  }
}
