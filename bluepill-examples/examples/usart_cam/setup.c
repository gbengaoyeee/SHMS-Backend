#include "setup.h"
#include "systick.h"

void clock_setup(void)
{
	rcc_clock_setup_in_hse_8mhz_out_72mhz();

	/* Enable INTERNAL_LED_PORT clock. */
	rcc_periph_clock_enable(RCC_GPIOA);
	rcc_periph_clock_enable(RCC_INTERNAL_LED);

	/* Enable clocks for GPIO port B (for GPIO_USART1_TX) and USART1. */
	rcc_periph_clock_enable(RCC_USART1);
	rcc_periph_clock_enable(RCC_DMA1);
}

void usart_setup(void)
{

	nvic_set_priority(NVIC_USART1_IRQ, 16);
	nvic_enable_irq(NVIC_USART1_IRQ);

	gpio_set_mode(GPIOA, GPIO_MODE_OUTPUT_50_MHZ,
		      GPIO_CNF_INPUT_PULL_UPDOWN, GPIO_USART1_TX);
	gpio_set_mode(GPIOA, GPIO_MODE_INPUT, GPIO_CNF_OUTPUT_ALTFN_PUSHPULL,
		      GPIO_USART1_RX);

	/* Setup UART parameters. */
	usart_set_baudrate(USART1, 115200);
	usart_set_databits(USART1, 9);
	usart_set_stopbits(USART1, USART_STOPBITS_1);
	usart_set_mode(USART1, USART_MODE_TX_RX);
	usart_set_parity(USART1, USART_PARITY_EVEN);
	usart_set_flow_control(USART1, USART_FLOWCONTROL_NONE);

	/* Enable RX Interruptions to usart1_isr() function */
	usart_enable_rx_interrupt(USART1);

	/* Finally enable the USART. */
	usart_enable(USART1);
}

void gpio_setup(void)
{

	rcc_periph_clock_enable(RCC_INTERNAL_LED);
	/* Set GPIO12 (in GPIO port C) to 'output push-pull'. */
	gpio_set_mode(INTERNAL_LED_PORT, GPIO_MODE_OUTPUT_2_MHZ,
		      GPIO_CNF_OUTPUT_PUSHPULL, INTERNAL_LED);
}

void setup()
{
	/* Change interrupt vector table location to avoid conflict with */
	/* serial bootloader interrupt vectors */
	SCB_VTOR = (uint32_t)0x08000000;
	clock_setup();
	gpio_setup();
	usart_setup();
	systick_setup();
}
