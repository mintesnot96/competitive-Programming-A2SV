class Solution:
  def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    people = [(name, height) for name, height in zip(names, heights)]
    sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
    sorted_names = [person[0] for person in sorted_people]
    return sorted_names





# https://leetcode.com/problems/sort-the-people/description/
