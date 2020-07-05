public class TurkeyTestDrive {
    public static void main(String[] args) {
        DonaldDuck duck = new DonaldDuck();
        Turkey duckAdapter = new DuckAdapter(duck);

        System.out.println("The Duck Adapter says...");
        for(int i = 0; i < 4; i++){

            System.out.println(i+1+"...");
            duckAdapter.gobble();
            duckAdapter.fly();
        }
    }
}
