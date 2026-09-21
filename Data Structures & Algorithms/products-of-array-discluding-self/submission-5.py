class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            products[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products
        
    def productExceptSelfY(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            # if i == 0:
            #     prefix_product.append(num)
            # else:
            prefix_product.append(nums[i] * prefix_product[-1])
        # prefix_product.pop()
        # prefix_product.insert(0, 1)

        suffix_product = [1]
        for i in range(len(nums) - 1, 0, -1):
            # if i == len(nums) - 1:
            #     suffix_product.insert(0, nums[i])
            # else:
            suffix_product.insert(0, nums[i] * suffix_product[0])
        # suffix_product.pop(0)
        # suffix_product.append(1)

        return [ prefix_product[i] * suffix_product[i] for i in range(len(nums)) ]

            