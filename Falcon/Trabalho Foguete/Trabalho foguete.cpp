#ifdef __APPLE__ // MacOS
	#define GL_SILENCE_DEPRECATION
	#include <GLUT/glut.h>
	#include <OpenGL/gl.h>
	#include <OpenGL/glu.h>
#else // Windows e Linux
	#include <GL/glut.h>
	#include <GL/gl.h>
	#include <GL/glu.h>
#endif

#define ESC 27
#define M_PI 3.14159265f

float R,G,B;

#include <cstdlib>
#include <cmath>

void init(void);
void reshape(int w, int h);
void keyboard(unsigned char key, int x, int y);
void display(void);

int main(int argc, char** argv){
	glutInit(&argc, argv); // Passagens de parametros C para o glut
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB); // Selecao do Modo do Display e do Sistema de cor utilizado
    glutInitWindowSize (900, 512);  // Tamanho da janela do OpenGL
    glutInitWindowPosition (100, 100); //Posicao inicial da janela do OpenGL
    glutCreateWindow ("Computcao Grafica: TrabalhoFoguete/OpenGL"); // Da nome para uma janela OpenGL
    init(); // Chama a funcao init();
    glutReshapeFunc(reshape); //funcao callback para redesenhar a tela
    glutDisplayFunc(display); //funcao callback de desenho
    glutKeyboardFunc(keyboard); //funcao callback do teclado
    glutMainLoop(); // executa o loop do OpenGL
    return EXIT_SUCCESS; // retorna 0 para o tipo inteiro da funcao main()
}

void init(void){
    glClearColor(0.1, 0.2, 0.4, 1.0); 
    R = 0.0;
    G = 0.0;
    B = 0.0;
}

void keyboard(unsigned char key, int x, int y){
    switch (key) {
        case ESC: exit(EXIT_SUCCESS); break; 
    }
}

void reshape(int w, int h) {
	
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	glViewport(0, 0, w, h);
	
	glOrtho (-(w/2), (w/2),-(h/2),(h/2), -1 ,1);
	glMatrixMode(GL_MODELVIEW);
}

void desenhaCirculo(float raio, int num_linhas,bool preenchido){
    int i;
    GLfloat angulo;
    angulo = (2 * M_PI) / num_linhas; 
 
    if(preenchido) glBegin(GL_TRIANGLE_FAN);  
    else glBegin(GL_LINE_LOOP);   
    
    for(i = 1; i <= num_linhas; i++) 
    {
        glVertex2f(-raio*sin(i * angulo) , raio*cos(i * angulo));
	}
    glEnd(); 
}

void desenhaEstrela(float tamanho) {
    glBegin(GL_TRIANGLES);
        glVertex2f(-tamanho, -tamanho/2);
        glVertex2f(tamanho, -tamanho/2);
        glVertex2f(0, tamanho);

        glVertex2f(-tamanho, tamanho/2);
        glVertex2f(tamanho, tamanho/2);
        glVertex2f(0, -tamanho);
    glEnd();
}

void desenhaRetangulo(float largura, float altura) {
    glBegin(GL_POLYGON);
        glVertex2f(-largura/2, -altura/2);
        glVertex2f(largura/2, -altura/2);
        glVertex2f(largura/2, altura/2);
        glVertex2f(-largura/2, altura/2);
    glEnd();
}

void display (void){
	glClear(GL_COLOR_BUFFER_BIT); 
	glLoadIdentity();
	
	//desenho da lua
	glPushMatrix();
        glTranslatef(250, 150, 0);
        glColor3f(0.9, 0.9, 0.8); 
        desenhaCirculo(100, 100, true);

		glColor3f(0.8, 0.8, 0.7);
        glPushMatrix();
        	glTranslatef(0, 50, 0);
        	desenhaCirculo(25, 50, true);
		glPopMatrix();

        glPushMatrix();
        	glTranslatef(50, -30, 0);
        	desenhaCirculo(25, 50, true);
		glPopMatrix();
		
        glPushMatrix();
  			glTranslatef(-45, -30, 0);
        	desenhaCirculo(25, 50, true);
		glPopMatrix();
    glPopMatrix();
    
    //desenho das estrelas
    glColor3f(1.0, 1.0, 0.0);

    glPushMatrix();
        glTranslatef(-330, 175, 0);
        desenhaEstrela(25);
    glPopMatrix();

    glPushMatrix();
        glTranslatef(20, 200, 0);
        desenhaEstrela(23);
    glPopMatrix();

    glPushMatrix();
        glTranslatef(150, 30, 0);
        desenhaEstrela(18);
    glPopMatrix();

    glPushMatrix();
        glTranslatef(0, -50, 0);
        desenhaEstrela(20);
    glPopMatrix();

    glPushMatrix();
        glTranslatef(270, -150, 0);
        desenhaEstrela(22);
    glPopMatrix();
	
	//desenho do foguete
    glPushMatrix();
        glTranslatef(-250, -50, 0);   
        glRotatef(-45, 0, 0, 1);       
		
        // Corpo
        glColor3f(0.8, 0.8, 0.8);     // cinza claro
        desenhaRetangulo(100, 250);
        
        glPushMatrix();
			glColor3f(0.2, 0.4, 0.7);
			glTranslatef(0, -120, 0);
			glRotatef(90, 0, 0, 1);
			desenhaRetangulo(18, 100);
        glPopMatrix();
        

        // Ponta 
        glColor3f(1.0, 0.0, 0.0);
        glTranslatef(0, 50, 0);
        glBegin(GL_TRIANGLES);
            glVertex2f(-50, 75); 
            glVertex2f(50, 75);  
            glVertex2f(0, 150);  
        glEnd();

        // Asas laterais
        
		glScalef(2.0, 2.0, 0.0);
		glPushMatrix();
			glTranslatef(-33, -3, 0);		
			glRotatef(56, 0, 0, 1);
	            glBegin(GL_POLYGON);
		            glVertex2f(-30, -30);  
		            glVertex2f(-60, -10);  
		            glVertex2f(-90, -30);  
		            glVertex2f(-60, -50);  
				glEnd();
		glPopMatrix();
		
		glPushMatrix();
			glTranslatef(33, -3, 0);
			glRotatef(-56, 0, 0, 1);
			glBegin(GL_POLYGON);
            glVertex2f(30, -30);  
            glVertex2f(60, -10);  
            glVertex2f(90, -30);  
            glVertex2f(60, -50);  
        glEnd();
		glPopMatrix();
        
        // Janela
        glPushMatrix();
	        glColor3f(0.1, 0.1, 0.2);   // borda escura
	        desenhaCirculo(22, 50, true);
	        glColor3f(0.2, 0.4, 0.7);   // azul
	        desenhaCirculo(18, 50, true);
		glPopMatrix();

        // Fogo (triângulos embaixo)
        glPushMatrix();
        glTranslatef(0, 3, 0);
        glScalef(1.26, 1.2, 1);
	        glBegin(GL_TRIANGLES);
	            glColor3f(1.0, 0.6, 0.0); // laranja
	            glVertex2f(-20, -75);
	            glVertex2f(20, -75);
	            glVertex2f(0, -120);
	
	            glColor3f(1.0, 1.0, 0.0); // amarelo
	            glVertex2f(-10, -75);
	            glVertex2f(10, -75);
	            glVertex2f(0, -100);
	        glEnd();
	        
	        glPushMatrix();
		        glColor3f(1.0, 0.0, 0.0);
		        glTranslatef(0, -65, 0);
		        desenhaRetangulo(5, 35);
	        glPopMatrix();
	        
		glPopMatrix();

    glPopMatrix();
	glFlush();
}