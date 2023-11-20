module led_blink (
    i_clock,
    i_enable,
    i_switch_1,
    i_switch_2,
    o_led
);

    input i_clock;
    input i_enable;
    input i_switch_1;
    input i_switch_2;
    output o_led;

    // Constants to define the frequency of the clock.
    // The clock frequency is 25 kHz.
    // Formula: (25 kHz / 100 Hz * 50% duty cycle)
    // So for 100 Hz : 25,000 / 100 * 50 = 125
    parameter c_CNT_100HZ = 125;
    parameter c_CNT_50HZ = 250;
    parameter c_CNT_10HZ = 1250;
    parameter c_CNT_1HZ = 12500;

    // These signals are used to count the clock cycles.
    reg [31:0] r_CNT_100HZ = 0;
    reg [31:0] r_CNT_50HZ = 0;
    reg [31:0] r_CNT_10HZ = 0;
    reg [31:0] r_CNT_1HZ = 0;

    // These signals will toggle the LED.
    reg r_TOGGLE_100HZ = 1'b0;
    reg r_TOGGLE_50HZ  = 1'b0;
    reg r_TOGGLE_10HZ  = 1'b0;
    reg r_TOGGLE_1HZ   = 1'b0;

    // One bit select signal for the LED.
    reg r_LED_SELECT;
    wire w_LED_SELECT;

    begin
        // All always blocks toggle a specific signal at a different frequency.
        // They all run continuously even if the switches are not selecting their particular output.

        always @ (posedge i_clock)
            begin
                if (r_CNT_100HZ == c_CNT_100HZ-1) // -1, since counter starts at 0
                    begin        
                        r_TOGGLE_100HZ <= !r_TOGGLE_100HZ;
                        r_CNT_100HZ    <= 0;
                    end
                else
                    r_CNT_100HZ <= r_CNT_100HZ + 1;
            end


        always @ (posedge i_clock)
            begin
                if (r_CNT_50HZ == c_CNT_50HZ) // -1, since counter starts at 0
                    begin
                        r_TOGGLE_50HZ <= !r_TOGGLE_50HZ;
                        r_CNT_50HZ    <= 0;    
                    end
                else
                    r_CNT_50HZ <= r_CNT_50HZ + 1;
            end


        always @ (posedge i_clock)
            begin
                if (r_CNT_10HZ == c_CNT_10HZ) // -1, since counter starts at 0
                    begin
                        r_TOGGLE_10HZ <= !r_TOGGLE_10HZ;
                        r_CNT_10HZ    <= 0;    
                    end
                else
                    r_CNT_10HZ <= r_CNT_10HZ + 1;
            end

        always @ (posedge i_clock)
            begin
                if (r_CNT_1HZ == c_CNT_1HZ) // -1, since counter starts at 0
                    begin
                        r_TOGGLE_1HZ <= !r_TOGGLE_1HZ;
                        r_CNT_1HZ    <= 0;    
                    end
                else
                    r_CNT_1HZ <= r_CNT_1HZ + 1;
            end


        // Add a multiplexer to select the LED output.
        // The LED output is selected by the switchi inputs.
        always @(*)
        begin
            case ({i_switch_1, i_switch_2}) // Concatenation Operator { }
                2'b11 : r_LED_SELECT <= r_TOGGLE_1HZ;
                2'b10 : r_LED_SELECT <= r_TOGGLE_10HZ;
                2'b01 : r_LED_SELECT <= r_TOGGLE_50HZ;
                2'b00 : r_LED_SELECT <= r_TOGGLE_100HZ;
            endcase
        end

        // Assign the LED output.
        assign o_led = r_LED_SELECT & i_enable;

    end

endmodule