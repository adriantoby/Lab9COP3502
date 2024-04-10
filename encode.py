def encode(nums: str) -> str:
  encoded = ""
  for num in nums:
    encoded += str(int(num) + 3)

  return encoded