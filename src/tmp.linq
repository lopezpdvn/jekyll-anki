<Query Kind="Statements">
  <Output>DataGrids</Output>
</Query>

//////////////////////////////////////////////////
// one line
(int first, int second)[] x = new[]
          { (1, 2), (3, 4), (5, 6), (7, 8) };

string[] q =
  (from e in x
   select $"({e.first}, {e.second})")
  .ToArray();
        
foreach(string s in q) s.Dump();