class Solution:
    def question(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sanity check on data source

        # option list may not be provided explicitly,
        # but deferred implicitly for data manipulation convenience.
        #  eg. #17, #78 and #79  use 'index'

        # it's convenient to give backtrack function defaults, so there's no need to remember to add them on first calling
        def backtrack(current_path, option_list):
            # working on current level
            if not sanity_check:
                return

            if ending_condition:
                result.append(current_path)
                return

            # record current path data into result list
            # can be in the form by index manipulation

            for item in option_list:
                if pruning_condition:
                    continue

                # make decision/change state, may need to do sanity check first
                # may need to update option list
                updated_path = current_path.append(item)

                #  go to next layer of decision tree
                # sometimes the path and option lists can even be modified directly in calling backtrack()
                backtrack(updated_path, "updated options")

                # cancel decision/recover state,
                # or don't do anything when backtracking is done with updated_path, ie. a clone of current_path

                current_path.pop()

        current_path = []
        option_list = []
        backtrack(current_path, option_list)

        return result
