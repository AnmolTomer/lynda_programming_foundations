// The Duck Superclass
public abstract class Duck {
    FlyBehavior flyBehavior; // 2 behaviors in Duck class fly and quack Behavior, used to give a duck its quacking and flying behavior.
    QuackBehavior quackBehavior;

    public Duck() { }

    public void setFlyBehavior(FlyBehavior fb) {
        this.flyBehavior = fb;
    }

    public void setQuackBehavior(QuackBehavior qb) {
        this.quackBehavior = qb;
    }

    abstract void display(); // Abstract method display

    public void performFly(){
        flyBehavior.fly();
    } // For duck to fly, goes to flyBehavior and gets the value of fly()

    public void performQuack(){ // performQuack() goes to quackBehavior
        quackBehavior.quack();
    }

    public void swim() {
        System.out.println("All ducks float, even decoys!");
    } // Works for all concrete ducks.

}
