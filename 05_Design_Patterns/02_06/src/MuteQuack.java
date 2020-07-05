public class MuteQuack implements QuackBehavior {
// All quack behaviors implement QuackBehavior
    public void quack() {
        System.out.println("<< Silence >>");
    }
}
