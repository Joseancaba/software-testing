# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


class TestWhiteBoxMore(unittest.TestCase):
    """Extra unit tests for white-box scenarios."""

    def test_check_number_status(self):
        """Checks number status function."""
        self.assertEqual(check_number_status(0), "Zero")
        self.assertEqual(check_number_status(1), "Positive")
        self.assertEqual(check_number_status(-1), "Negative")
        with self.assertRaises(TypeError):
            check_number_status("R")  # Invalid type should raise

    def test_validate_password(self):
        """Checks password validation function."""
        self.assertFalse(validate_password(""))  # Empty password
        self.assertFalse(validate_password("password"))  # No uppercase
        self.assertFalse(validate_password("Password"))  # No digit
        self.assertFalse(validate_password("Password1"))  # No special char
        self.assertTrue(validate_password("Password1!"))  # Valid password

    def test_calculate_total_discount(self):
        """Checks total discount calculation function."""
        self.assertEqual(calculate_total_discount(99.9), 0)  # <100 → 0%
        self.assertEqual(calculate_total_discount(100), 10.0)  # 10% at 100
        self.assertEqual(calculate_total_discount(500), 50.0)  # 10% at 500
        self.assertAlmostEqual(
            calculate_total_discount(500.01), 100.002, places=3
        )  # >500 → 20%

    def test_calculate_order_total(self):
        """Checks order total calculation function."""
        self.assertAlmostEqual(
            calculate_order_total([{"quantity": 1, "price": 1}]), 1.0, places=2
        )
        self.assertAlmostEqual(
            calculate_order_total([{"quantity": 5, "price": 1}]), 5.0, places=2
        )
        self.assertAlmostEqual(
            calculate_order_total([{"quantity": 6, "price": 1}]), 0.95 * 6, places=2
        )
        self.assertAlmostEqual(
            calculate_order_total([{"quantity": 10, "price": 1}]), 0.95 * 10, places=2
        )
        self.assertAlmostEqual(
            calculate_order_total([{"quantity": 11, "price": 1}]), 0.9 * 11, places=2
        )

    def test_calculate_items_shipping_cost(self):
        """Checks items shipping cost calculation function."""
        self.assertEqual(calculate_items_shipping_cost([{"weight": 0}], "standard"), 10)
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 5.0001}], "standard"), 15
        )  # justo arriba de 5
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 10}], "standard"), 15
        )  # límite superior del tramo medio
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 10.0001}], "standard"), 20
        )  # justo arriba de 10
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 5}], "express"), 20
        )  # límite inferior
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 5.0001}], "express"), 30
        )  # justo arriba de 5
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 10}], "express"), 30
        )  # límite superior del tramo medio
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 10.0001}], "express"), 40
        )  # justo arriba de 10
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(
                [{"weight": 5}], "overnight"
            )  # invalid shipping type

    def test_validate_login(self):
        """Checks login validation function."""
        self.assertEqual(validate_login("user5", "p" * 8), "Login Successful")  # 5 & 8
        self.assertEqual(
            validate_login("u" * 20, "p" * 15), "Login Successful"
        )  # 20 & 15
        # Fallos justo fuera de rango
        self.assertEqual(validate_login("u" * 4, "p" * 8), "Login Failed")  # username 4
        self.assertEqual(
            validate_login("u" * 21, "p" * 8), "Login Failed"
        )  # username 21
        self.assertEqual(validate_login("u" * 5, "p" * 7), "Login Failed")  # password 7
        self.assertEqual(
            validate_login("u" * 5, "p" * 16), "Login Failed"
        )  # password 16

    def test_verify_age(self):
        """Elegibilidad por edad: 18..65 inclusive."""
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_categorize_product(self):
        """Categorías por precio con límites inclusivos."""
        self.assertEqual(categorize_product(9), "Category D")
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")
        self.assertEqual(categorize_product(201), "Category D")

    def test_validate_email(self):
        """Validación de email por longitud y presencia de '@' y '.'."""
        self.assertEqual(validate_email("a@b.c"), "Valid Email")  # len 5
        self.assertEqual(
            validate_email(("a" * 38) + "@example.com"), "Valid Email"
        )  # len 50
        self.assertEqual(validate_email("a@b."), "Invalid Email")  # len 4 (corto)
        self.assertEqual(
            validate_email(("a" * 39) + "@example.com"), "Invalid Email"
        )  # len 51 (largo)

    def test_celsius_to_fahrenheit(self):
        """Conversión válida solo en [-100, 100]; fuera retorna mensaje de error."""
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_traffic_light(self):
        """Checks initial state and full cycle: Red -> Green -> Yellow -> Red -> Green."""
        tl = TrafficLight()

        self.assertEqual(tl.state, "Red")  # estado inicial

        tl.change_state()
        self.assertEqual(tl.state, "Green")  # Red -> Green

        tl.change_state()
        self.assertEqual(tl.state, "Yellow")  # Green -> Yellow

        tl.change_state()
        self.assertEqual(tl.state, "Red")  # Yellow -> Red

        tl.change_state()
        self.assertEqual(tl.state, "Green")  # inicia nuevo ciclo
