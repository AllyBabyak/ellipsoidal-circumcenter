using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using EllipsoidCircumcenter;

namespace EllipsoidCircumcenterTests
{
    [TestClass]
    public class VectorTests
    {
        [TestMethod]
        public void VectorCrossProduct_Test()
        {
            Coordinates.Vector vectorA = new Coordinates.Vector(1, 2, 3);
            Coordinates.Vector vectorB = new Coordinates.Vector(4, 5, 6);

            Coordinates.Vector expected = new Coordinates.Vector(-3, 6, -3);
            Coordinates.Vector actual = Coordinates.VectorCrossProduct(vectorA, vectorB);
            
            Assert.AreEqual(expected.x, actual.x);
            Assert.AreEqual(expected.y, actual.y);
            Assert.AreEqual(expected.z, actual.z);
        }
        [TestMethod]
        public void Midpoint_Test()
        {
            Coordinates.CartesianPoint point1 = new Coordinates.CartesianPoint(1, 2, 3);
            Coordinates.CartesianPoint point2 = new Coordinates.CartesianPoint(-1, 4, 15);

            Coordinates.CartesianPoint expected = new Coordinates.CartesianPoint(0, 3, 9);
            Coordinates.CartesianPoint actual = Coordinates.Midpoint(point1, point2);

            Assert.AreEqual(expected.x, actual.x);
            Assert.AreEqual(expected.y, actual.y);
            Assert.AreEqual(expected.z, actual.z);
        }
        [TestMethod]
        public void VectorThroughTwoPoints_Test()
        {
            Coordinates.CartesianPoint point1 = new Coordinates.CartesianPoint(1, 2, 3);
            Coordinates.CartesianPoint point2 = new Coordinates.CartesianPoint(-1, 4, 15);

            Coordinates.Vector expected = new Coordinates.Vector(2, -2, -12);
            Coordinates.Vector actual = Coordinates.VectorThroughTwoPoints(point1, point2);

            Assert.AreEqual(expected.x, actual.x);
            Assert.AreEqual(expected.y, actual.y);
            Assert.AreEqual(expected.z, actual.z);
        }
        [TestMethod]
        public void ThreePointPlaneNormal_Test()
        {
            Coordinates.CartesianPoint point1 = new Coordinates.CartesianPoint(1, 2, 3);
            Coordinates.CartesianPoint point2 = new Coordinates.CartesianPoint(-3, 5, -2);
            Coordinates.CartesianPoint point3 = new Coordinates.CartesianPoint(-2, -2, 1);

            Coordinates.Vector expected = new Coordinates.Vector(-26, 7, 25);
            Coordinates.Vector actual = Coordinates.ThreePointPlaneNormal(point1, point2, point3);

            Assert.AreEqual(expected.x, actual.x);
            Assert.AreEqual(expected.y, actual.y);
            Assert.AreEqual(expected.z, actual.z);
        }
        [TestMethod]
        public void LineIntersect_Test()
        {
            Coordinates.CartesianPoint point1 = new Coordinates.CartesianPoint(6, -2, 3);
            Coordinates.Vector vector1 = new Coordinates.Vector(-1, 8, -5);
            Coordinates.CartesianPoint point2 = new Coordinates.CartesianPoint(-2, -2, 1);
            Coordinates.Vector vector2 = new Coordinates.Vector(7, 8, -3);

            Coordinates.CartesianPoint expected = new Coordinates.CartesianPoint(5, 6, -2);
            Coordinates.CartesianPoint actual = Coordinates.LineIntersect(point1, vector1, point2, vector2);

            Assert.AreEqual(expected.x, actual.x);
            Assert.AreEqual(expected.y, actual.y);
            Assert.AreEqual(expected.z, actual.z);
        }
    }
}
