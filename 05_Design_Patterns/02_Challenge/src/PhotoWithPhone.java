import java.util.Scanner;

public class PhotoWithPhone {
    public static void main(String[] args) {
//        BasicCameraApp basicCamApp = new BasicCameraApp(); // Uncomment to run for BasicCameraApp
//        String share = getSharing();
//        switch (share){
//            case("t"): basicCamApp.setShareBehavior(new Txt());break;
//            case("s"): basicCamApp.setShareBehavior(new Social());break;
//            case("e"): basicCamApp.setShareBehavior(new Email());break;
//            default:
//                System.out.println("Enter choice.");break;
//        }
//        basicCamApp.take();
//        basicCamApp.edit();
//        basicCamApp.save();
//        basicCamApp.share();

        CameraPlusApp cameraPlusApp = new CameraPlusApp();
        String plusApp = getSharing2();
        switch (plusApp){
            case("t"): cameraPlusApp.setShareBehavior(new Txt());break;
            case("s"): cameraPlusApp.setShareBehavior(new Social());break;
            case("e"): cameraPlusApp.setShareBehavior(new Email());break;
        }
        cameraPlusApp.take();
        cameraPlusApp.edit();
        cameraPlusApp.save();
        cameraPlusApp.share();
    }

//    public static String getSharing()
//    {
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Share with txt (t), email (e) or social media (s)?");
//        String appName = sc.next().toLowerCase();
//        sc.close();
//        return appName;
//    }

    public static String getSharing2()
    {
        Scanner sc2 = new Scanner(System.in);
        System.out.println("Share with txt (t), email (e) or social media (s)?");
        String appName2 = sc2.next().toLowerCase();
        sc2.close();
        return appName2;
    }
}
