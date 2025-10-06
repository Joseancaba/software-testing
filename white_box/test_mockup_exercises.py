# -*- coding: utf-8 -*-
"""
Unit tests for mock up examples.
"""
import subprocess
import unittest
from unittest.mock import mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestDataFetcher(unittest.TestCase):
    """
    Tests for fetch_data_from_api
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Should return JSON data when request succeeds
        """
        # Configuramos el mock para simular la respuesta
        mock_get.return_value.json.return_value = {"status": "ok"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"status": "ok"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """
    Tests for read_data_from_file
    """

    @patch("builtins.open", new_callable=mock_open, read_data="mock content")
    def test_read_data_from_file_success(self, mock_file):
        """
        Should read file content successfully
        """
        content = read_data_from_file("fakefile.txt")
        self.assertEqual(content, "mock content")
        mock_file.assert_called_once_with("fakefile.txt", encoding="utf-8")

    def test_read_data_from_file_not_found(self):
        """
        Should raise FileNotFoundError if file does not exist
        """
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("missing.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Tests for execute_command
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Should return stdout when command executes successfully
        """
        mock_run.return_value = subprocess.CompletedProcess(
            args=["echo", "hello"], returncode=0, stdout="hello\n", stderr=""
        )

        output = execute_command(["echo", "hello"])
        self.assertEqual(output, "hello\n")
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Should raise CalledProcessError if command fails
        """
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="fakecmd", output="", stderr="error"
        )

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["fakecmd"])


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Tests for perform_action_based_on_time
    """

    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_perform_action_before_10(self, mock_time):
        """
        Should return Action A if time < 10
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time", return_value=20)
    def test_perform_action_after_10(self, mock_time):
        """
        Should return Action B if time >= 10
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()


if __name__ == "__main__":
    unittest.main()
