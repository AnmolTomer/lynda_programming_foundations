public class DonaldDuck extends Duck{ // extends duck, so inherits quack and fly behavior.
    public DonaldDuck(){ // Concrete Duck example
        quackBehavior = new Quack();
        flyBehavior = new FlyWithWings();
    }
    public void display(){
        System.out.println("I'm Donald Duck!");
    }
}
