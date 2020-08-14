class Solution:
    def question(self, nums: List[int]) -> List[List[int]]:

        result = []

        # option list may not be provided explicitly,
        # but deferred implicitly for data manipulation convenience.
        #  eg. #78 and #17 use 'index'

        # it's convenient to give backtrack function defaults, so there's no need to remember to add them on first calling
        def backtrack(current_path=[], option_list=[]):
            if ending_condition:
                return

            # record current path data into result list
            result.append(current_path)

            for item in option_list:
                # make decision, may need to do sanity check first
                # may need to update option list
                updated_path = current_path.append(item)

                #  go to next layer of decision tree
                # sometimes the path and option lists can even be modified directly in calling backtrack()
                backtrack(updated_path, option_list)

                # cancel decision,
                # or don't do anything when backtracking meets ending condition
                current_path.pop()

        backtrack()

        return result
