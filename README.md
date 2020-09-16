# CBIDOC
Cascading Behavior and Information Diffusion in Overlapping Clusters

# How to implement.

## Main
  
### Argument

--saveGraph(default = False)
True로 설정할 시, 그래프 데이터를 .gpickle데이터로 변환한다.  
이 때, ".community.txt"과 ".ungraph.txt"파일이 있어야한다.  
".community.txt" : 각 줄마다 같은 community에 속한 node number가 있어야하며 \t으로 구분된다.  
".ungraph.txt" : 각 줄마다 edge로 연결된 두 개의 node number가 있어야하며 \t으로 구분된다.  
  
--GraphName(default = "KarateClub")  
Diffusion 결과를 보고자 하는 Graph의 이름을 입력한다.  
  
--case(default = "DFOA")
후보로 DFOA(diffusion from overlap),  
         CDIOA(diffusion into overlap with compatibility),  
         CDFOA(diffusion from overlap with compatibility)가 있다.  
  
--q(default = 0)  
default값일 때 random하게 q의 값을 정한다.  
Compatibility가 없을 때, Behavior A(새로운 정보)를 노드가 습득하기 위한 threshold이다.  

--c(default = 0)  
default값일 때 random하게 c의 값을 정한다.  
Compatibility가 있을 때, Behavior AB를 노드가 습득하기 위해 필요한 cost이다.  

○ Main.py -h를 통해 각 argument에 대한 설명을 확인할 수 있다.  

○ 실험을 진행하기 위해 linux환경에서는 python3 Main.py --argument를 입력하면 된다.
