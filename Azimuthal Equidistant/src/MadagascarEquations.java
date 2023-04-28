public class MadagascarEquations {
    // Constants:
    static double semiMajorAxis = 6378206.4; // International 1924: 6378388, Clarke: 6378206.4
    static double eccent2 = 0.00676866; // International 1924: 0.006722670, Clarke: 0.00676866
    static double eccent = Math.sqrt(eccent2); //
    static double k0 = 1.0;
    // Frequently Used Equations:
    static double tanTimes(double phi){
        double inTan,inEx,whole;
        inTan = Math.PI/4 + phi/2;
        inEx = (1-eccent * Math.sin(phi))/(1+eccent * Math.sin(phi));
        whole = Math.tan(inTan) * Math.pow(inEx, eccent/2);
        return whole;
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
    // Constants to Calculate:
    static double bValue(double phiC){
        double top,bottom,B;
        top = eccent2 * Math.pow(Math.cos(phiC),4);
        bottom = 1 - eccent2;
        B = Math.sqrt(1 + top/bottom);
        return B;
    }
    static double phiSValue(double phiC, double B){
        double phiS;
        phiS = Math.asin(Math.sin(phiC)/B);
        return phiS;
    }
    static double rValue(double phiC){
        double top,bottom,R;
        top = Math.sqrt(1-eccent2);
        bottom = 1-eccent2*Math.pow(Math.sin(phiC),2);
        R = semiMajorAxis * k0 * (top/bottom);
        return R;
    }
    static double cValue(double phiS,double phiC,double B){
        double ln1,ln2,C;
        ln1 = Math.tan(Math.PI/4 + phiS/2);
        ln2 = tanTimes(phiC);
        C = Math.log(ln1) - B * Math.log(ln2);
        return C;
    }
    // Forward Equations:
    static double lValue(double B, double lambda, double lambdaC){
        return B * (lambda - lambdaC);
    }
    static double qValue(double C, double B, double phi){
        return C + B * Math.log(tanTimes(phi));
    }
    static double pValue(double q){
        return 2 * Math.atan(Math.exp(q)) - Math.PI/2;
    }
    static double uValue(double P, double L, double phiS){
        return Math.cos(P)*Math.cos(L)*Math.cos(phiS) + Math.sin(P)*Math.sin(phiS);
    }
    static double vValue(double P, double L, double phiS){
        return Math.cos(P)*Math.cos(L)*Math.cos(phiS) - Math.sin(P)*Math.sin(phiS);
    }
    static double wValue(double P, double L){
        return Math.cos(P) * Math.sin(L);
    }
    static double dValue(double U, double V){
        return Math.sqrt(Math.pow(U,2)+Math.pow(V,2));
    }
    static double lPrimeVal(double d, double V, double U){
        double lPrime;
        if (d == 0) {lPrime = 0;} else {lPrime = V / (U+d);}
        return lPrime;
    }
    static double pPrimeVal(double d, double W){
        double pPrime;
        if (d == 0){pPrime = Math.signum(W) * (Math.PI/2);} else {pPrime = Math.atan(W/d);}
        return pPrime;
    }
    static Complex hValue(double lPrime, double pPrime){
        double real = lPrime;
        double imag = Math.log(Math.tan(Math.PI/4 + pPrime/2));
        return new Complex(real,imag);
    }
    static Complex gValue(double alphaC){
        double real = (1-Math.cos(2*alphaC))/12;
        double imag = (Math.sin(2*alphaC))/12;
        return new Complex(real,imag);
    }
    static double eCoord(double Ec,double R,Complex H, Complex G){
        Complex a = H.plus(G.times(H.times(H.times(H))));
        return Ec + R*a.im();
    }
    static double nCoord(double Nc, double R, Complex H, Complex G){
        Complex a = H.plus(G.times(H.times(H.times(H))));
        return Nc + R*a.re();
    }
    public static void main(String[] args){
        double Paris = dmsToRadians("2 20'14.025\"");
        double phiC = -0.329867;
        double lambdaC = 0.76969;
        double phi = dmsToRadians("-12 15'19.725\"");
        double lambda = dmsToRadians("47 1'0.198\"")+Paris;
        double azimuth = 0.329867; // 1.179738031
        double B = bValue(phiC);
        double phiS = phiSValue(phiC, B);
        double R = rValue(phiC);
        double C = cValue(phiS, phiC,B);
        double L = lValue(B,lambda,lambdaC);
        double q = qValue(C,B,phi);
        double P = pValue(q);
        double U = uValue(P,L,phiS);
        double V = vValue(P,L,phiS);
        double W = wValue(P,L);
        double d = dValue(U,V);
        double LPrime = lPrimeVal(d,V,U);
        double PPrime = pPrimeVal(d,W);
        Complex H = hValue(LPrime, PPrime);
        Complex G = gValue(azimuth);
        double E = eCoord(400000,R,H,G);
        double N = nCoord(800000,R,H,G);
        System.out.println(E);
        System.out.println(N);
    }
}
