using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EllipsoidCircumcenter
{
    public class Program
    {
        public static void CircumcenterCartesian()
        {

            Console.WriteLine("Enter point 1 in cartesian coordidates");
            Coordinates.CartesianPoint point1 = Coordinates.StringToCartesian(Console.ReadLine());

            Console.WriteLine("Enter point 2 in cartesian coordidates");
            Coordinates.CartesianPoint point2 = Coordinates.StringToCartesian(Console.ReadLine());

            Console.WriteLine("Enter point 3 in cartesian coordidates");
            Coordinates.CartesianPoint point3 = Coordinates.StringToCartesian(Console.ReadLine());

            Coordinates.CartesianPoint center = Coordinates.CartesianCircumcenter(point1, point2, point3);
            Coordinates.CartesianPoint planarCircumcenter = Coordinates.ThreePointPlanarCircumcenter(point1,point2,point3);

            Console.WriteLine("The center is " + Coordinates.CartesianToString(center));

            Console.WriteLine("The planar center is " + Coordinates.CartesianToString(planarCircumcenter));
        }
        public static void CircumcenterDegrees()
        {
            Console.WriteLine("Enter point 1 in geodetic degrees");
            Coordinates.GeodeticDegrees point1 = Coordinates.StringToDegrees(Console.ReadLine());

            Console.WriteLine("Enter point 2 in geodetic degrees");
            Coordinates.GeodeticDegrees point2 = Coordinates.StringToDegrees(Console.ReadLine());

            Console.WriteLine("Enter point 3 in geodetic degrees");
            Coordinates.GeodeticDegrees point3 = Coordinates.StringToDegrees(Console.ReadLine());

            Coordinates.GeodeticDegrees center = Coordinates.DegreesCircumcenter(point1, point2, point3);

            Console.WriteLine("The center is " + Coordinates.DegreesToString(center));
        }
        public static void Main(string[] args)
        {
            CircumcenterDegrees();
        }
    }
}
