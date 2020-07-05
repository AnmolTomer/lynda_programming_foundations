public abstract class PhoneCameraApp {
    ShareBehavior shareBehavior;

    public void setShareBehavior(ShareBehavior sb){
        this.shareBehavior = sb;
    }

    public void take(){
        System.out.println("Taking the photo!");
    }

    public void share(){
        shareBehavior.share();
    }

    public void save(){
        System.out.println("Saving the photo!");
    }

    public abstract void edit();

}
