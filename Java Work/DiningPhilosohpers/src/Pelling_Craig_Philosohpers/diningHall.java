package Pelling_Craig_Philosohpers;

import java.util.concurrent.Semaphore;

public class diningHall{
    private static Semaphore s1 = new Semaphore(1);
    private static Semaphore s2 = new Semaphore(1);
    private static Semaphore s3 = new Semaphore(1);
    private static Semaphore s4 = new Semaphore(1);
    private static Semaphore s5 = new Semaphore(1);
    private static Semaphore screen = new Semaphore(1);
    private static Philosopher[] pl;

    public static void main(String[] args) throws Exception {

        Philosopher plato = new Philosopher("Plato", s1, s2, screen);
        Philosopher aristotle = new Philosopher("Aristotle", s2, s3, screen);
        Philosopher socrates = new Philosopher("Socrates", s4, s3, screen);
        Philosopher confucius = new Philosopher("Confucius", s4, s5, screen);
        Philosopher laozi = new Philosopher("Laozi", s1, s5, screen);
        pl = new Philosopher[]{plato, aristotle, socrates, confucius, laozi};

        wineAndDine();
    }

    /**
     *  Starts and joins each Philosopher in the Philosopher list
     */
    private static void wineAndDine() {
        for(Philosopher p : pl) {
          try{
              screen.acquire();
          } catch (Exception ignore){}
          p.start();
          screen.release();
        }
    }
}
