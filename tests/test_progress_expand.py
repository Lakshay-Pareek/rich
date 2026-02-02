"""Tests for expand parameter in progress.track function"""
import io
from rich.progress import track
from rich.console import Console


def test_track_expand_parameter_exists():
    """Test that track function accepts expand parameter"""
    result = list(track(range(10), expand=True))
    assert len(result) == 10


def test_track_expand_true_uses_full_width():
    """Test that expand=True creates full-width progress bar"""
    console = Console(file=io.StringIO(), width=100, legacy_windows=False)
    
    with console.capture() as capture:
        for _ in track(range(5), console=console, expand=True):
            pass
    
    output = capture.get()
    assert len(output) > 90


def test_track_expand_false_uses_default_width():
    """Test that expand=False maintains current behavior"""
    console = Console(file=io.StringIO(), width=100, legacy_windows=False)
    
    with console.capture() as capture:
        for _ in track(range(5), console=console, expand=False):
            pass
    
    output_false = capture.get()
    
    with console.capture() as capture:
        for _ in track(range(5), console=console):
            pass
    
    output_default = capture.get()
    
    assert len(output_false) < 300
    assert abs(len(output_false) - len(output_default)) < 50


def test_track_backward_compatibility():
    """Test that existing track usage still works"""
    result1 = list(track(range(10)))
    result2 = list(track(range(10), description="Test"))
    result3 = list(track(range(10), total=10))
    result4 = list(track(range(10), show_speed=False))
    
    assert len(result1) == 10
    assert len(result2) == 10
    assert len(result3) == 10
    assert len(result4) == 10


def test_track_expand_with_other_parameters():
    """Test that expand works with other parameters"""
    result = list(track(
        range(10),
        description="Processing",
        expand=True,
        show_speed=True
    ))
    assert len(result) == 10
