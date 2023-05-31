from machine import Pin, ADC, PWM
from utime import sleep_ms, sleep

button = Pin(0, Pin.IN, Pin.PULL_UP)   # Internal pull-up
led = Pin(1, Pin.OUT)
State = 0                              # 0 means that the light is currently off
soundIn = ADC(26)
pwm_out = PWM(Pin(4))                   # Configure PWM output on GP4

if __name__ == '__main__':
    while True:
        print(button.value())
        if button.value() == 0:      
            if State == 0:
                led.value(1)
                sleep_ms(100)        
                while button.value() == 0:
                    pass             
                State = 1
            else:
                led.value(0)
                sleep_ms(100)        
                while button.value() == 0:
                    pass              
                State = 0

        # read values of ADC
        reading = soundIn.read_u16()
        pwm_duty = int(reading / 65535 * 1023)  # Scale ADC reading to 0-1023 range for PWM duty cycle
        pwm_out.duty_u16(pwm_duty)

        print("ADC:", reading)
        sleep(0.2)                     
