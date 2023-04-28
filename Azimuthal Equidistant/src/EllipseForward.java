public class EllipseForward {
    // Constants:
    static double semiMajorAxis = 6378388;
    static double eccent = Math.sqrt(0.006722670);
    static double k0 = 1.0;
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
        bottom = Math.cos(1+Math.sin(chi1)*Math.sin(chi)+Math.cos(phi1)*Math.cos(phi)*Math.cos(lambda-lambda0));
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


}
