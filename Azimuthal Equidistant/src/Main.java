import java.util.Scanner;

public class Main {
    // Constants:
    static double semiMajorAxis = 6378206.4; // International 1924: 6378388, Clarke: 6378206.4
    static double eccent = Math.sqrt(0.00676866); // International 1924: 0.006722670, Clarke: 0.00676866
    static double k0 = 1.0;
   // Conversion Equations:
    static double degreesToRadians(double angle) {
        return angle * Math.PI / 180;
    }
    static double dmsToRadians(String dmsAngle){
        int degIndex = dmsAngle.indexOf(' ');
        int minIndex = dmsAngle.indexOf('\'');
        int secIndex = dmsAngle.indexOf('"');
        double d = Double.valueOf(dmsAngle.substring(0,degIndex));
        double m = Double.valueOf(dmsAngle.substring(degIndex+1,minIndex));
        double s = Double.valueOf(dmsAngle.substring(minIndex+1,secIndex));
        double rad = Math.PI * (d+m/60+s/3600)/180;
        return rad;
    }
    // Spheroid Equations:
    static double xCoord(double A,double chi,double lambda, double lambda0) {
        double xVal;
        xVal = A * Math.cos(chi) * Math.sin(lambda-lambda0);
        return xVal;
    }
    static double yCoord(double A, double chi1, double chi, double lambda, double lambda0) {
        double yVal;
        yVal = A*(Math.cos(chi1)*Math.sin(chi) - Math.sin(chi1)*Math.cos(chi)*Math.cos(lambda-lambda0));
        return yVal;
    }
    static double aValue(double m1, double chi1, double chi,double phi1, double phi, double lambda, double lambda0) {
        double aVal,top,bottom;
        top = 2 * semiMajorAxis * k0 * m1;
        bottom = Math.cos(chi1)*(1+Math.sin(chi1)*Math.sin(chi)+Math.cos(phi1)*Math.cos(phi)*Math.cos(lambda-lambda0));
        aVal = top / bottom;
        return aVal;
    }
    static double mValue(double latitude) {
        double m = (Math.cos(latitude))/Math.sqrt(1 - Math.pow((eccent * Math.sin(latitude)),2));
        return m;
    }
    static double chiValue(double latitude) {
        double inTan, inEx, inATan, chi;
        inTan = Math.PI/4 + latitude/2;
        inEx = (1 - eccent * Math.sin(latitude))/(1 + eccent * Math.sin(latitude));
        inATan = (Math.tan(inTan) * Math.pow(inEx, eccent/2));
        chi = 2 * Math.atan(inATan) - Math.PI/2;
        return chi;
    }

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);

        //System.out.println("Enter latitude and longitude");

        //Float latitude = myObj.nextFloat();
        //Float longitude = myObj.nextFloat();

        double phi1 = dmsToRadians("15 11'05.6830\"");
        double lambda0 = dmsToRadians("145 44'29.9720\"");
        double phi = dmsToRadians("15 14'47.4930\"");
        double lambda = dmsToRadians("145 347'34.9080\"");
        double m1 = mValue(phi1);
        double chi1 = chiValue(phi1);
        double chi = chiValue(phi);
        double A = aValue(m1,chi1,chi,phi1,phi,lambda,lambda0);

        System.out.println(xCoord(A,chi,lambda,lambda0));
        System.out.println(yCoord(A,chi1,chi,lambda,lambda0));

        System.out.println(degreesToRadians(13.472466353));
        System.out.println(dmsToRadians("13 28'20.87887\""));
    }
}

