let currentValue = 0;

// Add event listener to the plus button
document.getElementById('plusButton').addEventListener('click', function () {
  const threshold = parseInt(document.getElementById('threshold').value, 10);

  // Logical error: Should use `<=` instead of `<`
  if (currentValue < threshold) {
    currentValue++;
    document.getElementById('value').textContent = currentValue;
  } else {
    alert('Value has reached the threshold.');
  }
});

// Add event listener to the reset button
document.getElementById('resetButton').addEventListener('click', function () {
  currentValue = 0;
  document.getElementById('value').textContent = currentValue;
  alert('Value has been reset.');
});
