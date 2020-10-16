package Pelling_Craig_Philosohpers;
import java.util.Random;
import java.util.concurrent.Semaphore;

public class Philosopher extends Thread{

	private volatile String philosopherName; // The name of the dude
    private volatile int stateOfMind; // 0: thinking   1: hungry   2: Eating
    private volatile Semaphore chopStick1;
    private volatile Semaphore chopStick2;
    private volatile Semaphore screen;

    private final int EATING_TIME = 2000;

    public Philosopher(String name, Semaphore chopStick1, Semaphore chopStick2, Semaphore screen) {
        this.philosopherName = name;
        this.stateOfMind = 0;
        this.chopStick1 = chopStick1;
        this.chopStick2 = chopStick2;
        this.screen = screen;
        printState("Thinking");
    }


    @Override
    public void run() {

        Random rand = new Random();
        while (true) {

            int num = rand.nextInt(60);
            if(num == 0) {
                try {
                    screen.acquire();
                } catch (Exception ignored) {}
                this.changState();
                screen.release();
            }

            // if the state is Eating try to acquire the chopsticks
            if(this.stateOfMind == 1){
                //System.out.println("State is 2: " + this.philosopherName);
                try {
                    screen.acquire();
                    chopStick1.acquire();
                    //System.out.println("Acquiring Semaphore 1: " +  this.philosopherName);
                    chopStick2.acquire();
                    //System.out.println("Acquiring Semaphore 2: " +  this.philosopherName);
                } catch (Exception e) {
                    this.reverseState();
                }
               //printState("Eating");
                this.changState();
                this.screen.release();
                try {
					this.sleep(EATING_TIME);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
                this.chopStick1.release();
                this.chopStick2.release();
            }
        }
    }


    /**
     * Changes the state of the Philosopher is follows:
     *  - state is 0 => 1
     *  - state is 1 => 2
     *  - state is 2 => 0
     */
    public void changState() {
        switch (this.stateOfMind) {
            case 0:
                this.stateOfMind = 1;
                printState("Hungry");
                break;
            case 1 :
                this.stateOfMind = 2;
                // Do not print state here we will do that in the run function
                printState("Eating");
                break;
            case 2:
                this.stateOfMind = 0;
                printState("Thinking");
                break;
        }
    }

    private void printState(String state) {
        System.out.println(String.format("Philosopher %1$s is %2$s", this.philosopherName, state));
    }

    /**
     * Sets the Philosopher's state back to hungry if there are no chop sticks available
     */
    public void reverseState(){
        this.stateOfMind = 1;
    }

    public String getPhilosopherName() {
        return philosopherName;
    }

    public int getStateOfMind() {
        return stateOfMind;
    }
    
}
