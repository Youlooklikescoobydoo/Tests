#include <stdio.h>
#include <stdlib.h>
#include <SDL.h>

#define SDL_OK	0
#define TRUE	1
#define FALSE	0

#define WIDTH	1024
#define HEIGHT	768

typedef int BOOL;

typedef enum setColour_t {
	RED,
	GREEN,
	BLUE
} setColour_t;

int main() {
	if (initializeSdl() == FALSE) return -1;
	if (initializeSdlWindow() == FALSE) return -2;

	while (isEventLoopRunning()) {
		setBackground();
		createRectangle();
		renderAll();
	}

	cleanUpSdl();

	return 0;

	BOOL initializeSdl()
	{
		if (SDL_Init(SDL_INIT_VIDEO) != SDL_OK) {
			printf("Error while initializing SDL: %s", SDL_GetError());
			return FALSE;
		}

		return TRUE;
	}

	BOOL initializeSdlWindow()
	{
		if (SDL_CreateWindowAndRenderer(WIDTH, HEIGHT, SDL_WINDOW_RESIZABLE, &_window, &_r))
		{
			printf("Error while creating SDL Window %s", SDL_GetError()):
		}

		SDL_SetWindowTitle(_window, "SDL2 in C, Colors")

		return TRUE;
	}

	BOOL isEventLoopRunning()
	{
		SDL_Event sdlEvent;

		while (SDL_PollEvent(&sdlEvent) != SDL_OK) {
			switch (sdlEvent.type)
			{
			case SDL_KEYUP:
				swith (sdlEvent.key.keysym.sym) {
					case SDLK_ESCAPE:
						return FALSE;
					case SDLK_r:
						_redContent = 255;
						_greenContent = 0;
						_blueContent = 0:
						_setColour = RED;
						break;
					case SDLK_g:
						_redContent = 0;
						_greenContent = 255;
						_blueContent = 0;
						_setColour = GREEN;

				}
			}
		}
	}
	void cleanUpSdl()
	{
		SDL_DestroyRenderer(_renderer);
		SDL_DestroyWindow(_window);
		SDL_Quit();
	}
}