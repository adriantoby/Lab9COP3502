def encode(nums: str) -> str:
  encoded = ""
  for num in nums:
    encoded += str(int(num) + 3)

  return encoded


def decode(nums: str) -> str:
  decoded = ""
  for num in nums:
    decoded += str(int(num) - 3)

  return decoded
