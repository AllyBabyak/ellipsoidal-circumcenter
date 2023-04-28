public class RiemannBack {
    // Constants of Earth:
    static double semiMajorAxis = 6378206.4; // International 1924: 6378388, Clarke: 6378206.4
    static double eccent2 = 0.00676866; // International 1924: 0.006722670, Clarke: 0.00676866
    static double eccent = Math.sqrt(eccent2); //

    // Conversion Equations:
    static double degreesToRadians(double angle) {
        return angle * Math.PI / 180;
    }
    static double radiansToDegrees(double angle) {
        return angle * 180 / Math.PI;
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

    // Constants to calculate:
    static double etaValue2(double centreLatitude){
        return (eccent2 / (1-eccent2)) * Math.pow(Math.cos(centreLatitude),2);
    }
    static double vValue2(double centreLatitude){
        return 1+etaValue2(centreLatitude);
    }
    static double tValue(double centreLat){
        return Math.tan(centreLat);
    }
    static double nValue(double centreLatitude){
        return semiMajorAxis / (Math.sqrt(1 - eccent2 * Math.pow(Math.sin(centreLatitude),2)));
    }
    static double cValue(double centreLatitude){
        return Math.cos(centreLatitude);
    }

    // Coefficient formulas
    static double coeff10(double N, double C){
        return 1 / (N*C);
    }
    static double coeff11(double T, double N, double C){
        return T / (Math.pow(N,2)*C);
    }
    static double coeff30(double T,double N,double C){
        return -(Math.pow(T,2))/(3*Math.pow(N,3)*C);
    }
    static double coeff12(double T,double N,double C,double eta){
        return (1+3*Math.pow(T,2)+eta)/(3*Math.pow(N,3)*C);
    }
    static double coeff31(double T,double N,double C,double eta){
        return -(T*(1+3*Math.pow(T,2))+eta)/(3*Math.pow(N,4)*C);
    }
    static double coeff13(double T,double N,double C,double eta){
        return (T * (2+3*Math.pow(T,2)+eta-Math.pow(eta,2)))/(3*Math.pow(N,4)*C);
    }
    static double coeff50(double T,double N,double C,double eta){
        return (Math.pow(T,2)*(1+3*Math.pow(T,2)+eta))/(15*Math.pow(N,5)*C);
    }
    static double coeff32(double T,double N,double C,double eta){
        double top,bottom;
        top = 1+20*Math.pow(T,2)+30*Math.pow(T,4)+eta*(2+13*Math.pow(T,2))+Math.pow(eta,2)*(1-7*Math.pow(T,2));
        bottom = 15*Math.pow(N,5)*C;
        return top/bottom;
    }
    static double coeff14(double T,double N,double C,double eta){
        double top1,top2,bottom;
        top1 = 2+15*Math.pow(T,2)+15*Math.pow(T,4)+3*eta*(1+2*Math.pow(T,2));
        top2 = -3*Math.pow(eta*T,2)-Math.pow(eta,6)*(1-6*Math.pow(T,2));
        bottom = 15*Math.pow(N,5)*C;
        return (top1+top2)/bottom;
    }
    static double pointLongitude(double xCoord, double yCoord, double centreLong, double centreLat){
        double T,N,C,eta,Term10,Term11,Term30,Term12,Term31,Term13,Term50,Term32,Term14;
        T = tValue(centreLat);
        N = nValue(centreLat);
        C = cValue(centreLat);
        eta = etaValue2(centreLat);
        Term10 = coeff10(N,C)*xCoord;
        Term11 = coeff11(T,N,C)*xCoord*yCoord;
        Term30 = coeff30(T,N,C)*Math.pow(xCoord,3);
        Term12 = coeff12(T,N,C,eta)*xCoord*Math.pow(yCoord,2);
        Term31 = coeff31(T,N,C,eta)*Math.pow(xCoord,3)*yCoord;
        Term13 = coeff13(T,N,C,eta)*xCoord*Math.pow(yCoord,3);
        Term50 = coeff50(T,N,C,eta)*Math.pow(xCoord,5);
        Term32 = coeff32(T,N,C,eta)*Math.pow(xCoord,3)*Math.pow(yCoord,2);
        Term14 = coeff14(T,N,C,eta)*xCoord*Math.pow(yCoord,4);
        return  centreLong+Term10+Term11+Term30+Term12+Term31+Term13+Term50+Term32+Term14;
    }
    public static void main(String[] args){
        double cLat = degreesToRadians(15.18491194);
        double cLong = degreesToRadians(145.7416589);
        double x = 5518.21;
        double y = 6817.89;
        double radLong = pointLongitude(x,y,cLong,cLat);
        System.out.println(radiansToDegrees(radLong));
        System.out.println(145.7930300);
    }
}
