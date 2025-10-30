"""
找一个不交叉的方案? -> 难
简化:
  给定一些线条, 检查是否有交叉点
"""

"""
读取n个"人-鬼"pair, which is n lines
检查每一对线段, 是否有相交点
  任一步看到交叉点, 报告无效并退出
步骤做完, 没有退出既有效方案
"""

"""
    如何判断两线段存在交叉点?
    reference:
    blog.csdn.net/lesileqin/article/details/97051299

    a. 跨立
        叉积 (ca × cd) * (cb × cd)
        完整的跨立实验： 需要双向检查。
    b. 提前优化
       “包围盒”（Bounding Box提前批准一些线段

"""

"""
1. 定义数据结构

  def orientation(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:

    计算三点p, q, r的相对方向。
    
    返回:
        0 : p, q, r 共线 (On the same path)
        1 : 顺时针方向 / 右转 (Clockwise / Right Turn)
        -1: 逆时针方向 / 左转 (Counter-Clockwise / Left Turn)

    # 叉积计算公式
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0  # 共线
    
    # 根据正负号返回方向
    return 1 if val > 0 else -1
"""

def orientation(p: tuple, q: tuple, r: tuple) -> int:
    """
    Fundamental tool: uses cross product to determine orientation.
    Like driving navigation: when going from p to q, is r on left, right, or straight ahead?
    
    Args:
        p (tuple): Starting point
        q (tuple): Destination point  
        r (tuple): Point to check relative to line pq
        
    Returns:
        0 : p, q, r are collinear (point lies on the line)
        1 : Clockwise / Right turn
       -1 : Counter-clockwise / Left turn
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
    
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def on_segment(p: tuple, q: tuple, r: tuple) -> bool:
    """
    Helper function: when p, q, r are collinear, check if point q lies on segment pr.
    
    Args:
        p, r: Segment endpoints
        q: Point to check
        
    Returns:
        True if q lies on segment pr, False otherwise
    """
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def segments_intersect(seg1: tuple, seg2: tuple) -> bool:
    """
    Determine if two line segments seg1 and seg2 intersect.
    Segment format: ((x1, y1), (x2, y2))
    Uses parametric line intersection method.
    
    Args:
        seg1, seg2: Two line segments to check
        
    Returns:
        True if segments intersect, False otherwise
    """
    p1, q1 = seg1
    p2, q2 = seg2
    
    # --- Step 1: Fast Exclusion Test (Bounding Box Check) ---
    # Check if bounding boxes overlap. If not, segments cannot intersect.
    if not (max(p1[0], q1[0]) >= min(p2[0], q2[0]) and
            max(p2[0], q2[0]) >= min(p1[0], q1[0]) and
            max(p1[1], q1[1]) >= min(p2[1], q2[1]) and
            max(p2[1], q2[1]) >= min(p1[1], q1[1])):
        return False  # Bounding boxes don't overlap, early return for optimization
    
    # --- Step 2: Parametric Line Intersection ---
    # Line 1: P1 + t1 * (Q1 - P1), t1 in [0, 1]
    # Line 2: P2 + t2 * (Q2 - P2), t2 in [0, 1]
    
    x1, y1 = p1
    x2, y2 = q1
    x3, y3 = p2
    x4, y4 = q2
    
    # Calculate denominators
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    # If lines are parallel (denominator is zero)
    if abs(denom) < 1e-10:
        # Check if segments are collinear and overlapping
        # Use cross product to check if all points are collinear
        if abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) < 1e-10:
            # Segments are collinear, check for overlap
            # Project onto x-axis (or y-axis if x-range is small)
            if abs(x2 - x1) > abs(y2 - y1):
                # Project onto x-axis
                t1_min, t1_max = min(x1, x2), max(x1, x2)
                t2_min, t2_max = min(x3, x4), max(x3, x4)
            else:
                # Project onto y-axis
                t1_min, t1_max = min(y1, y2), max(y1, y2)
                t2_min, t2_max = min(y3, y4), max(y3, y4)
            
            # Check for overlap
            return max(t1_min, t2_min) <= min(t1_max, t2_max)
        else:
            # Lines are parallel but not collinear
            return False
    
    # Calculate intersection parameters
    t1 = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    t2 = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
    
    # Check if intersection point lies on both segments
    return 0 <= t1 <= 1 and 0 <= t2 <= 1

def read_ghostbusters_file(filename: str):
    """
    Read Ghostbusters input file and extract line segments.
    
    Args:
        filename (str): Path to input file
        
    Returns:
        list: List of segments in format ((buster_x, buster_y), (ghost_x, ghost_y))
    """
    segments = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())  # First line: number of Ghostbusters
        
        for i in range(1, n + 1):
            if i >= len(lines):
                break
                
            line = lines[i].strip()
            if not line:
                continue
                
            parts = line.split()
            
            # Extract coordinates: format is "B x1 y1 G x2 y2"
            buster_x = int(parts[1])  # After 'B'
            buster_y = int(parts[2])  
            ghost_x = int(parts[4])   # After 'G'  
            ghost_y = int(parts[5])
            
            segment = ((buster_x, buster_y), (ghost_x, ghost_y))
            segments.append(segment)
    
    return segments

def check_ghostbusters_solution(filename: str) -> str:
    """
    Main function to check if all ghosts can be eliminated without crossing streams.
    
    Args:
        filename (str): Path to input file
        
    Returns:
        str: Result message indicating whether all ghosts were eliminated
    """
    # Read segments from file
    segments = read_ghostbusters_file(filename)
    
    n = len(segments)
    intersection_found = False
    
    # Double loop to check all possible segment pairs
    # range(i + 1, n) ensures we don't check duplicate pairs
    for i in range(n):
        for j in range(i + 1, n):
            seg1 = segments[i]
            seg2 = segments[j]
            
            if segments_intersect(seg1, seg2):
                intersection_found = True
                # Found one intersection is enough, can stop searching
                break
        
        if intersection_found:
            break
    
    # Return appropriate result message
    if intersection_found:
        return "All Ghosts: were not eliminated"
    else:
        return "All Ghosts: were eliminated"

# ==============================================================================
# Main Execution
# ==============================================================================

if __name__ == "__main__":
    import sys
    
    # Use command line argument if provided, otherwise use default test file
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # For testing with your provided file
        input_file = "ghostbusters_input_0.txt"
    
    try:
        result = check_ghostbusters_solution(input_file)
        print(result)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

# ==============================================================================
# Test Function for Multiple Files
# ==============================================================================

def test_all_files():
    """
    Test function to run all input files and compare with expected answers.
    Useful for batch testing with your provided test cases.
    """
    test_cases = 9  # Based on your file numbering 0-8
    
    for i in range(test_cases):
        input_file = f"ghostbusters_input_{i}.txt"
        answer_file = f"ghostbusters_ans_{i}.txt"
        
        try:
            # Calculate result
            result = check_ghostbusters_solution(input_file)
            
            # Read expected answer
            with open(answer_file, 'r') as f:
                expected = f.read().strip()
            
            # Check if result matches expected
            status = "PASS" if result == expected else "FAIL"
            print(f"Test {i}: {status} | Result: {result} | Expected: {expected}")
            
        except FileNotFoundError:
            print(f"Test {i}: File not found - {input_file} or {answer_file}")
        except Exception as e:
            print(f"Test {i}: ERROR - {e}")


test_all_files() # Uncomment this to run all tests!!!