"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output"""
        cmd = [sys.executable, '-m', 'src.cli'] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli('add', '5', '3')
        assert result.returncode == 0
        assert result.stdout.strip() == '8'

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli('multiply', '4', '7')
        assert result.returncode == 0
        assert result.stdout.strip() == '28'

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli('divide', '15', '3')
        assert result.returncode == 0
        assert result.stdout.strip() == '5'

    def test_cli_sqrt_integration(self):
        """Test CLI can perform square root"""
        result = self.run_cli('square_root', '16')
        assert result.returncode == 0
        assert result.stdout.strip() == '4'

    def test_cli_error_handling_integration(self):
        """Test CLI properly handles calculator errors"""
        result = self.run_cli('divide', '10', '0')
        assert result.returncode == 1
        assert 'Cannot divide by zero' in result.stdout

    def test_cli_invalid_operation_integration(self):
        """Test CLI handles invalid operations"""
        result = self.run_cli('invalid', '1', '2')
        assert result.returncode == 1
        assert 'Unknown operation' in result.stdout


class TestCalculatorModuleIntegration:
    """Test calculator module functions work together"""

    def test_chained_operations(self):
        """Test using results from one operation in another"""
        from src.calculator import a

