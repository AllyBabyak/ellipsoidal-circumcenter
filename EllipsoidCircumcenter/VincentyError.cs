using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EllipsoidCircumcenter
{
    public class VincentyError
    {
        private static double SemiMajorAxis = 6378137.0;
        private static double SemiMinorAxis = 6356752.314245;
        private static double Eccentricity = (Math.Pow(SemiMajorAxis, 2) - Math.Pow(SemiMinorAxis, 2)) / Math.Pow(SemiMajorAxis, 2);
        private static double Flattening = 1 / 298.257223563;

        public static double VincentyDistance(Coordinates.GeodeticRadians point1, Coordinates.GeodeticRadians point2)
        {
            if ((point1.latitude == point2.latitude) & (point1.latitude == 0)) { return SemiMajorAxis * Math.Abs(point1.longitude - point2.longitude); }
            else
            {
                double u1 = Math.Atan((1 - Flattening) * Math.Tan(point1.latitude));
                double u2 = Math.Atan((1 - Flattening) * Math.Tan(point2.latitude));
                double longitudeStart = point2.longitude - point1.longitude;

                double sinU1 = Math.Sin(u1);
                double sinU2 = Math.Sin(u2);
                double cosU1 = Math.Cos(u1);
                double cosU2 = Math.Cos(u2);

                double tolerance = Math.Pow(10, -12);
                double lambda = longitudeStart;

                double sinAlpha = 0;
                double sinSigma = 0;
                double cos2SigmaM = 0;
                double cosSigma = 0;
                double sigma = 0;
                double difference = 1;

                do
                {
                    double a = cosU1 * sinU2 - sinU1 * cosU2 * Math.Cos(lambda);
                    sinSigma = Math.Sqrt(Math.Pow(cosU2 * Math.Sin(lambda),2) + Math.Pow(a,2));
                    cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * Math.Cos(lambda);
                    sigma = Math.Atan2(sinSigma, cosSigma);
                    sinAlpha = (cosU1 * cosU2 * Math.Sin(lambda)) / sinSigma;
                    cos2SigmaM = cosSigma - (2 * sinU1 * sinU2) / (1 - Math.Pow(sinAlpha,2));
                    double b = (Flattening / 16) * (1 - Math.Pow(sinAlpha,2)) * (4 + Flattening * (4 - 3 * (1 - Math.Pow(sinAlpha,2))));
                    double newLambda = lambda;
                    double c = cos2SigmaM + b * cosSigma * (-1 + 2 * Math.Pow(cos2SigmaM, 2));
                    lambda = longitudeStart + (1 - b) * Flattening * sinAlpha * (sigma + b * sinSigma * c);

                    difference = Math.Abs(lambda - newLambda);
                } while (difference  > tolerance);

                double d = (1 - Math.Pow(sinAlpha, 2)) * ((Math.Pow(SemiMajorAxis, 2) - Math.Pow(SemiMinorAxis,2)) / Math.Pow(SemiMinorAxis, 2));
                double e = 1 + (d / 16384) * (4096 + d * (-768 + d * (320 - 175 * d)));
                double f = (d / 1024) * (256 + d * (-128 + d * (74 - 47 * d)));
                double g = (-3 + 4 * Math.Pow(sinSigma, 2)) * (-3 + 4 * Math.Pow(cos2SigmaM, 2));
                double deltaSigma = f * sinSigma * (cos2SigmaM + 1 / 4 * f * (cosSigma * (-1 + 2 * Math.Pow(cos2SigmaM,2) - f / 6 * cos2SigmaM * g)));

                return SemiMinorAxis * e * (sigma - deltaSigma);
            }
        }
        public static double Error(Coordinates.GeodeticRadians point1,  Coordinates.GeodeticRadians point2, Coordinates.GeodeticRadians point3, Coordinates.GeodeticRadians center)
        {
            double distance1 = VincentyDistance(point1, center);
            double distance2 = VincentyDistance(point2, center);
            double distance3 = VincentyDistance(point3, center);

            double error = Math.Max(distance1, Math.Max(distance2, distance3)) - Math.Min(distance1, Math.Min(distance2, distance3));
            return error;
        }
        public static double ErrorCartesian(Coordinates.CartesianPoint point1, Coordinates.CartesianPoint point2, Coordinates.CartesianPoint point3, Coordinates.CartesianPoint center)
        {
            Coordinates.GeodeticRadians radP1 = Coordinates.CartesianToRadians(point1);
            Coordinates.GeodeticRadians radP2 = Coordinates.CartesianToRadians(point2);
            Coordinates.GeodeticRadians radP3 = Coordinates.CartesianToRadians(point3);
            Coordinates.GeodeticRadians radC = Coordinates.CartesianToRadians(center);

            return Error(radP1, radP2, radP3, radC);
        }
        public static double ErrorDegrees(Coordinates.GeodeticDegrees point1, Coordinates.GeodeticDegrees point2, Coordinates.GeodeticDegrees point3, Coordinates.GeodeticDegrees center)
        {
            Coordinates.GeodeticRadians radP1 = Coordinates.DegreesToRadians(point1);
            Coordinates.GeodeticRadians radP2 = Coordinates.DegreesToRadians(point2);
            Coordinates.GeodeticRadians radP3 = Coordinates.DegreesToRadians(point3);
            Coordinates.GeodeticRadians radC = Coordinates.DegreesToRadians(center);

            return Error(radP1, radP2, radP3, radC);
        }
        public static double VincentyDistanceCartesian(Coordinates.CartesianPoint point1, Coordinates.CartesianPoint point2)
        {
            Coordinates.GeodeticRadians radP1 = Coordinates.CartesianToRadians(point1);
            Coordinates.GeodeticRadians radP2 = Coordinates.CartesianToRadians(point2);
            return VincentyDistance(radP1, radP2);
        }
        public static double VincentyDistanceDegrees(Coordinates.GeodeticDegrees point1, Coordinates.GeodeticDegrees point2)
        {
            Coordinates.GeodeticRadians radP1 = Coordinates.DegreesToRadians(point1);
            Coordinates.GeodeticRadians radP2 = Coordinates.DegreesToRadians(point2);
            return VincentyDistance(radP1, radP2);
        }
        public static double AverageDistance(Coordinates.GeodeticRadians point1, Coordinates.GeodeticRadians point2, Coordinates.GeodeticRadians point3, Coordinates.GeodeticRadians center)
        {
            double distance1 = VincentyDistance(point1, center);
            double distance2 = VincentyDistance(point2, center);
            double distance3 = VincentyDistance(point3, center);

            double average = (distance1 + distance2 + distance3) / 3;
            return average;
        }
        public static double AverageDistanceDegrees(Coordinates.GeodeticDegrees point1, Coordinates.GeodeticDegrees point2, Coordinates.GeodeticDegrees point3, Coordinates.GeodeticDegrees center)
        {
            Coordinates.GeodeticRadians radP1 = Coordinates.DegreesToRadians(point1);
            Coordinates.GeodeticRadians radP2 = Coordinates.DegreesToRadians(point2);
            Coordinates.GeodeticRadians radP3 = Coordinates.DegreesToRadians(point3);
            Coordinates.GeodeticRadians radC = Coordinates.DegreesToRadians(center);

            return AverageDistance(radP1, radP2, radP3, radC);
        }
        public static Coordinates.GeodeticDegrees SphericalCircumcenterDegrees(Coordinates.GeodeticDegrees point1, Coordinates.GeodeticDegrees point2, Coordinates.GeodeticDegrees point3)
        {
            Coordinates.CartesianPoint point1C = Coordinates.DegreesToCartesian(point1);
            Coordinates.CartesianPoint point2C = Coordinates.DegreesToCartesian(point2);
            Coordinates.CartesianPoint point3C = Coordinates.DegreesToCartesian(point3);

            Coordinates.CartesianPoint centerC = Coordinates.ThreePointPlanarCircumcenter(point1C, point2C, point3C);

            return Coordinates.CartesianToDegrees(centerC);
        }
    }
}
