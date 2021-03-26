/* usbcdcdemo.c : USBCDC Example (adventure)
 * Warren Gay
 */
#include <FreeRTOS.h>
#include <task.h>
#include <semphr.h>
#include <stdio.h>
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/cm3/nvic.h>

#include "common.h"
#include "usbcdc.h"

static SemaphoreHandle_t sem_flash = 0;
static void
flasher(void *arg __attribute__((unused))) {

	for (;;) {
		xSemaphoreTake(sem_flash,portMAX_DELAY);
		gpio_toggle(GPIOC,GPIO13);
		xSemaphoreGive(sem_flash);
		vTaskDelay(pdMS_TO_TICKS(400));
	}
}
static void buzzer(void *arg __attribute__((unused))) {
	int i;
	rcc_periph_clock_disable(RCC_GPIOA);
	rcc_periph_clock_enable(RCC_GPIOA);
	gpio_set_mode(GPIOA,GPIO_MODE_OUTPUT_2_MHZ,GPIO_CNF_OUTPUT_PUSHPULL,GPIO8);
	
	for (;;) {
		gpio_clear(GPIOA,GPIO8);	
		for (i = 0; i < 1500; i++)	
			__asm__("nop");

		gpio_set(GPIOA,GPIO8);		
		for (i = 0; i < 1500; i++)	
			__asm__("nop");
	}

	
}
static void buzz(void *arg __attribute__((unused))) {
	int i;   
	for (;;) {
			gpio_clear(GPIOA,GPIO8);	
			for (i = 0; i < 2; i++)	
				__asm__("nop");

			gpio_set(GPIOA,GPIO8);		
			for (i = 0; i < 2; i++)	
				__asm__("nop");
		}
	

}
void
set_lamp(enum LampActions action) {
	static bool have = false;

	switch ( action ) {
	case Take:
		xTaskCreate(buzzer,"buzzer",100,NULL,configMAX_PRIORITIES-1,NULL);
		if ( have ) {
			xSemaphoreGive(sem_flash);
			
			have = false;
		}
		
		break;
	case Filled:
		if ( !have ) {
			xSemaphoreTake(sem_flash,portMAX_DELAY);
			gpio_clear(GPIOC,GPIO13); // LED on
			rcc_periph_clock_disable(RCC_GPIOA);
			have = true;
		}
		break;
	case Drop:
		//xTaskCreate(buzz,"buzz",100,NULL,configMAX_PRIORITIES-1,NULL);
		if ( !have ) {
			xSemaphoreTake(sem_flash,portMAX_DELAY);

			have = true;
		}
		gpio_set(GPIOC,GPIO13);		// LED off
		
		rcc_periph_clock_disable(RCC_GPIOA);
		break;
	}
}


int main(void) {
		
	rcc_clock_setup_in_hse_8mhz_out_72mhz();	// Use this for "blue pill"
	rcc_periph_clock_enable(RCC_GPIOC);
	gpio_set_mode(GPIOC,GPIO_MODE_OUTPUT_2_MHZ,GPIO_CNF_OUTPUT_PUSHPULL,GPIO13);
	
	usb_start();
	
	xTaskCreate(adventure,"game",300,NULL,configMAX_PRIORITIES-1,NULL);
	xTaskCreate(flasher,"flash",100,NULL,configMAX_PRIORITIES-1,NULL);
	sem_flash = xSemaphoreCreateMutex();
	set_lamp(Filled);

	vTaskStartScheduler();
	return 0;
}
