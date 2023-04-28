using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EllipsoidCircumcenter
{
    public class Coordinates
    {
        private static double SemiMajorAxis = 6378137.0;
        private static double SemiMinorAxis = 6356752.314245;
        private static double Eccentricity = (Math.Pow(SemiMajorAxis, 2) - Math.Pow(SemiMinorAxis, 2)) / Math.Pow(SemiMajorAxis, 2);

        public class GeodeticRadians
        {
            public double latitude;
            public double longitude;
            public GeodeticRadians(double latitude, double longitude)
            {
                this.latitude = latitude;
                this.longitude = longitude;
            }
        }
        public class GeodeticDegrees
        {
            public double latitude;
            public double longitude;
            public GeodeticDegrees(double latitude, double longitude)
            {
                this.latitude = latitude;
                this.longitude = longitude;
            }
        }
        public class CartesianPoint
        {
            public double x;
            public double y;
            public double z;
            public CartesianPoint(double x, double y, double z)
            {
                this.x = x;
                this.y = y;
                this.z = z;
            }
        }
        public class Vector
        {
            public double x;
            public double y;
            public double z;
            public Vector(double x, double y, double z)
            {
                this.x = x;
                this.y = y;
                this.z = z;
            }
        }
        public static string CartesianToString(CartesianPoint point)
        {
            string xVal = point.x.ToString();
            string yVal = point.y.ToString();
            string zVal = point.z.ToString();
            return "(" + xVal + "," + yVal + "," + zVal + ")";
        }
        public static CartesianPoint StringToCartesian(string str)
        {
            int firstComma = str.IndexOf(',');
            int lastComma = str.LastIndexOf(",");
            double xVal = double.Parse(str.Substring(1, firstComma - 1));
            double yVal = double.Parse(str.Substring(firstComma + 1, lastComma - firstComma - 1));
            double zVal = double.Parse(str.Substring(lastComma + 1, str.Length - lastComma - 2));
            return new CartesianPoint(xVal, yVal, zVal);
        }
        public static string RadiansToString(GeodeticRadians point)
        {
            string latitude = point.latitude.ToString();
            string longitude = point.longitude.ToString();
            return "(" + latitude + "," + longitude + ")";
        }
        public static GeodeticRadians StringToRadians(string str)
        {
            int comma = str.IndexOf(",");
            double latitude = double.Parse(str.Substring(1, comma - 1));
            double longitude = double.Parse(str.Substring(comma + 1, str.Length - comma - 2));
            return new GeodeticRadians(latitude, longitude);
        }
        public static string DegreesToString(GeodeticDegrees point)
        {
            string latitude = point.latitude.ToString();
            string longitude = point.longitude.ToString();
            return "(" + latitude + "," + longitude + ")";
        }
        public static GeodeticDegrees StringToDegrees(string str)
        {
            int comma = str.IndexOf(",");
            double latitude = double.Parse(str.Substring(1, comma - 1));
            double longitude = double.Parse(str.Substring(comma + 1, str.Length - comma - 2));
            return new GeodeticDegrees(latitude, longitude);
        }
        public static CartesianPoint RadiansToCartesian(GeodeticRadians point)
        {
            double N = SemiMajorAxis / Math.Sqrt(1 - (Eccentricity * Math.Pow(Math.Sin(point.latitude), 2)));
            double x = N * Math.Cos(point.latitude) * Math.Cos(point.longitude);
            double y = N * Math.Cos(point.latitude) * Math.Sin(point.longitude);
            double z = (1 - Eccentricity) * N * Math.Sin(point.latitude);
            CartesianPoint NewPoint = new CartesianPoint(x, y, z);
            return NewPoint;
        }
        public static GeodeticRadians CartesianToRadians(CartesianPoint point)
        {
            double fx = 2 * point.x / Math.Pow(SemiMajorAxis, 2);
            double fy = 2 * point.y / Math.Pow(SemiMajorAxis, 2);
            double fz = 2 * point.z / Math.Pow(SemiMinorAxis, 2);
            double bottom = Math.Sqrt(Math.Pow(fx, 2) + Math.Pow(fy, 2) + Math.Pow(fz, 2));
            double latitude = Math.Asin(Math.Abs(fz) / bottom);
            double longitude = Math.Atan2(point.y, point.x);
            if (point.z < 0) { latitude = -latitude; }
            GeodeticRadians NewPoint = new GeodeticRadians(latitude, longitude);
            
            return NewPoint;
        }
        public static GeodeticRadians DegreesToRadians(GeodeticDegrees point)
        {
            double rLat = point.latitude * Math.PI / 180;
            double rLong = point.longitude * Math.PI / 180;
            GeodeticRadians NewPoint = new GeodeticRadians(rLat, rLong);
            return NewPoint;
        }
        public static GeodeticDegrees RadiansToDegrees(GeodeticRadians point)
        {
            double dLat = point.latitude * 180 / Math.PI;
            double dLong = point.longitude * 180 / Math.PI;
            GeodeticDegrees NewPoint = new GeodeticDegrees(dLat, dLong);
            return NewPoint;
        }
        public static GeodeticDegrees CartesianToDegrees(CartesianPoint point)
        {
            GeodeticRadians rPoint = CartesianToRadians(point);
            GeodeticDegrees newPoint = RadiansToDegrees(rPoint);
            return newPoint;
        }
        public static CartesianPoint DegreesToCartesian(GeodeticDegrees point)
        {
            GeodeticRadians rPoint = DegreesToRadians(point);
            CartesianPoint newPoint = RadiansToCartesian(rPoint);
            return newPoint;
        }
        public static Vector VectorCrossProduct(Vector a, Vector b)
        {
            double x = a.y * b.z - a.z * b.y;
            double y = a.z * b.x - a.x * b.z;
            double z = a.x * b.y - a.y * b.x;
            return new Vector(x, y, z);
        }
        public static CartesianPoint Midpoint(CartesianPoint point1, CartesianPoint point2)
        {
            double x = (point1.x + point2.x) / 2;
            double y = (point1.y + point2.y) / 2;
            double z = (point1.z + point2.z) / 2;
            return new CartesianPoint(x, y, z);
        }
        public static Vector VectorThroughTwoPoints(CartesianPoint point1, CartesianPoint point2)
        {
            double x = point1.x - point2.x;
            double y = point1.y - point2.y;
            double z = point1.z - point2.z;
            return new Vector(x, y, z);
        }
        public static Vector ThreePointPlaneNormal(CartesianPoint point1, CartesianPoint point2, CartesianPoint point3)
        {
            Vector vector12 = VectorThroughTwoPoints(point1, point2);
            Vector vector13 = VectorThroughTwoPoints(point1, point3);
            return VectorCrossProduct(vector12, vector13);
        }
        public static CartesianPoint LineIntersect(CartesianPoint point1, Vector vector1, CartesianPoint point2, Vector vector2) // This is what causes problems at equator
        {
            
            double n = vector1.x * (point1.y - point2.y) + vector1.y * (point2.x - point1.x);
            double d = vector1.x * vector2.y - vector1.y * vector2.x;
            if (d == 0)
            {
                n = vector1.z * (point1.y - point2.y) + vector1.y * (point2.z - point1.z);
                d = vector1.z * vector2.y - vector1.y * vector2.z;
                if (d == 0)
                {
                    n = vector1.x * (point1.z - point2.z) + vector1.z * (point2.x - point1.x);
                    d = vector1.x * vector2.z - vector1.z * vector2.x;
                }
            }
            double scale = n / d;
            double x = point2.x + vector2.x * scale;
            double y = point2.y + vector2.y * scale;
            double z = point2.z + vector2.z * scale;
            return new CartesianPoint(x, y, z);
        }
        public static double StraightLineDistance(CartesianPoint point1, CartesianPoint point2)
        {
            return Math.Sqrt(Math.Pow(point2.x - point1.x, 2) + Math.Pow(point2.y - point1.y, 2) + Math.Pow(point2.z - point1.z, 2));
        }
        public static double CircumcenterError(CartesianPoint point1, CartesianPoint point2, CartesianPoint point3, CartesianPoint potentialCenter)
        {
            double distance1 = StraightLineDistance(point1, potentialCenter);
            double distance2 = StraightLineDistance(point2, potentialCenter);
            double distance3 = StraightLineDistance(point3, potentialCenter);
            double error = Math.Max(Math.Max(distance1, distance2), distance3) - Math.Min(Math.Min(distance1, distance2), distance3);
            return error;
        }
        static CartesianPoint BestCircumcenter(CartesianPoint point1, CartesianPoint point2, CartesianPoint point3, CartesianPoint center1, CartesianPoint center2, CartesianPoint center3)
        {
            double error1 = CircumcenterError(point1, point2, point3, center1);
            double error2 = CircumcenterError(point1, point2, point3, center2);
            double error3 = CircumcenterError(point1, point2, point3, center3);
            if ((error1 < error2) & (error1 < error3)) { return center1; }
            else if ((error2 < error1) & (error2 < error3)) { return center2; }
            else { return center3; }
        }
        static CartesianPoint CenterPick(CartesianPoint planarCenter, CartesianPoint intersection1, CartesianPoint intersection2)
        {
            double distance1 = StraightLineDistance(planarCenter, intersection1);
            double distance2 = StraightLineDistance(planarCenter, intersection2);
            if (distance1 < distance2) { return intersection1; }
            else { return intersection2; }
        }
        public static CartesianPoint ThreePointPlanarCircumcenter(CartesianPoint point1, CartesianPoint point2, CartesianPoint point3)
        {
            Vector pNormal = ThreePointPlaneNormal(point1, point2, point3);
            CartesianPoint midpoint12 = Midpoint(point1, point2);
            CartesianPoint midpoint13 = Midpoint(point1, point3);
            CartesianPoint midpoint23 = Midpoint(point2, point3);
            Vector vector12 = VectorThroughTwoPoints(point1, point2);
            Vector vector13 = VectorThroughTwoPoints(point1, point3);
            Vector vector23 = VectorThroughTwoPoints(point2, point3);
            Vector perp12 = VectorCrossProduct(vector12, pNormal);
            Vector perp13 = VectorCrossProduct(vector13, pNormal);
            Vector perp23 = VectorCrossProduct(vector23, pNormal);

            CartesianPoint intersect1 = LineIntersect(midpoint12, perp12, midpoint13, perp13);
            CartesianPoint intersect2 = LineIntersect(midpoint13, perp13, midpoint23, perp23);
            CartesianPoint intersect3 = LineIntersect(midpoint23, perp23, midpoint12, perp12);

            return BestCircumcenter(point1, point2, point3, intersect1, intersect2, intersect3);
        }
        static double QuadraticFormula(double a, double b, double c, bool positive)
        {
            double determinant = Math.Pow(b, 2) - 4 * a * c;
            if (determinant < 0) { return -b / (2 * a); }
            else if (positive) { return (-b + Math.Sqrt(determinant)) / (2 * a); }
            else { return (-b - Math.Sqrt(determinant)) / (2 * a); }
        }
        public static CartesianPoint IntersectionWithSpheroid(CartesianPoint point, Vector vector)
        {
            double a = (Math.Pow(vector.x, 2) + Math.Pow(vector.y, 2)) / Math.Pow(SemiMajorAxis, 2) + Math.Pow(vector.z, 2) / Math.Pow(SemiMinorAxis, 2);
            double b = 2 * ((vector.x * point.x + vector.y * point.y) / Math.Pow(SemiMajorAxis, 2) + (vector.z * point.z) / Math.Pow(SemiMinorAxis, 2));
            double c = (Math.Pow(point.x, 2) + Math.Pow(point.y, 2)) / Math.Pow(SemiMajorAxis, 2) + Math.Pow(point.z, 2) / Math.Pow(SemiMinorAxis, 2) - 1;
            if (Math.Abs(a) < Math.Pow(10,-12))
            {
                double scale = -c / b;
                double x = point.x + vector.x * scale;
                double y = point.y + vector.y * scale;
                double z = point.z + vector.z * scale;
                return new CartesianPoint(x, y, z);
            }
            else
            {
                double pScale = QuadraticFormula(a, b, c, true);
                double nScale = QuadraticFormula(a, b, c, false);

                double xP = point.x + vector.x * pScale;
                double yP = point.y + vector.y * pScale;
                double zP = point.z + vector.z * pScale;
                CartesianPoint pCenter = new CartesianPoint(xP, yP, zP);

                double xN = point.x + vector.x * nScale;
                double yN = point.y + vector.y * nScale;
                double zN = point.z + vector.z * nScale;
                CartesianPoint nCenter = new CartesianPoint(xN, yN, zN);

                return CenterPick(point, pCenter, nCenter);
            }
        }
        public static CartesianPoint CircumcenterOnXYPlane(Vector planeNormal, CartesianPoint planeCircumcenter)
        {
            double a = 1 + Math.Pow(planeNormal.y, 2) / Math.Pow(planeNormal.x, 2);
            double b = (2 * planeCircumcenter.y * planeNormal.y) / planeNormal.x - (2 * planeCircumcenter.x * Math.Pow(planeNormal.y, 2)) / Math.Pow(planeNormal.x, 2);
            double c = Math.Pow(planeCircumcenter.y, 2) - (2 * planeCircumcenter.y * planeNormal.y * planeCircumcenter.x) / planeNormal.x + Math.Pow(planeNormal.y * planeCircumcenter.x / planeNormal.x, 2) - Math.Pow(SemiMajorAxis, 2);

            double pX = QuadraticFormula(a, b, c, true);
            double nX = QuadraticFormula(a, b, c, false);

            double pY = planeCircumcenter.y + (planeNormal.y * (pX - planeCircumcenter.x)) / planeNormal.x;
            double nY = planeCircumcenter.y + (planeNormal.y * (nX - planeCircumcenter.x)) / planeNormal.x;

            CartesianPoint pCenter = new CartesianPoint(pX, pY, 0);
            CartesianPoint nCenter = new CartesianPoint(nX, nY, 0);

            return CenterPick(planeCircumcenter, pCenter, nCenter);
        }
        public static CartesianPoint CartesianCircumcenter(CartesianPoint point1, CartesianPoint point2, CartesianPoint point3)
        {
            Vector planeNormal = ThreePointPlaneNormal(point1, point2, point3);
            CartesianPoint planeCircumcenter = ThreePointPlanarCircumcenter(point1, point2, point3);
            if (Math.Abs(planeNormal.z) < Math.Pow(10, -6)) { return CircumcenterOnXYPlane(planeNormal, planeCircumcenter); }
            else { return IntersectionWithSpheroid(planeCircumcenter, planeNormal); }
        }
        public static GeodeticDegrees DegreesCircumcenter(GeodeticDegrees point1, GeodeticDegrees point2, GeodeticDegrees point3)
        {
            CartesianPoint point1C = DegreesToCartesian(point1);
            CartesianPoint point2C = DegreesToCartesian(point2);
            CartesianPoint point3C = DegreesToCartesian(point3);
            CartesianPoint center = CartesianCircumcenter(point1C, point2C, point3C);
            return CartesianToDegrees(center);
        }
    }
}
