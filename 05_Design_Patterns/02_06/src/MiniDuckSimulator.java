public class MiniDuckSimulator { // This is where we create and test duck behaviors
    public static void main(String[] args) {
        DonaldDuck donald = new DonaldDuck();
        FlyBehavior cantFly = () -> System.out.println("I can't fly!");
        QuackBehavior squeak = () -> System.out.println("Squeak!");
        RubberDuck rubberDuckie = new RubberDuck(cantFly,squeak);
        DecoyDuck decoyDuck = new DecoyDuck();

        Duck model = new ModelDuck();

        donald.performQuack();
        rubberDuckie.performQuack();
        decoyDuck.performQuack();

        model.performFly();
        model.setFlyBehavior(new FlyRedBull());
        model.performFly();

    }
}
