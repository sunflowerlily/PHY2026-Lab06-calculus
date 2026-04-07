# 第 6 周实验：数值微积分（微分 + 积分）

## 0. 物理引导

本周核心问题是：当解析表达式不可得或只有离散数据时，如何用数值方法稳定、可信地计算导数与积分。

- 数值微分：前差/后差/中心差分、截断误差与舍入误差、最优步长、Richardson 外推。
- 数值积分：梯形公式、Simpson 公式、自适应思想、Gauss-Legendre 积分。
- AI 审查重点：边界处理、步长与网格、误差解释、物理量量纲与极限行为。

本周任务严格对应讲义第 6 周（数值微积分）与 Newman Chapter 5（Integrals and Derivatives）中的训练主线。

---

## 1. 任务结构与分值

| 模块 | 内容 | 分值 | 难度 |
|---|---|---:|---|
| Lab1-Core A | 物理模型与基准函数定义 | 23 | L1 |
| Lab1-Core B | AI 毒药代码排雷与求解器重构 | 24 | L1/L2 |
| Lab1-Core C | 误差验证与可视化自动评分 | 23 | L1/L2 |
| Lab2-Bonus | Debye 热容积分与算法对比拓展 | 30 | L2/L3 |

---

## 2. 3人并行分工（无串行依赖）

| 成员任务 | 对应文件 | 核心交付 |
|---|---|---|
| 任务A（成员1） | `lab1_core/src/physics_model.py` | 定义当周函数模型、解析导数、解析积分基准与物理参数 |
| 任务B（成员2） | `lab1_core/src/solver.py`（修复 `solver_bad_ai.py`） | 修复数值算法与边界/步长漏洞，给出稳定实现 |
| 任务C（成员3） | `lab1_core/tests/test_core.py` + `lab1_core/notebook_core.ipynb` | 误差曲线、守恒/极限验证、自动测试闭环 |

要求：三人必须都有独立 commit 记录，否则对应任务记 0 分。

---

## 3. Lab1-Core（课堂 90 分钟，70 分）

### Task A（23分，L1）基础模型与参考真值

文件：`lab1_core/src/physics_model.py`

- 定义 `f_diff(x)=sin(x)` 及其解析导数 `df_diff(x)=cos(x)`。
- 定义 `f_int(x)=x**4-2x+1` 及其解析积分函数。
- 提供统一误差函数（绝对误差/相对误差）。

### Task B（24分，L1/L2）AI 毒药代码排雷

文件：`lab1_core/src/solver_bad_ai.py`、`lab1_core/src/solver.py`

- `solver_bad_ai.py` 含隐蔽错误（步长处理、Simpson 偶数约束、Richardson 系数误用）。
- 在 `solver.py` 中修复并实现：
  - 前差/后差/中心差分
  - 复合梯形积分
  - 复合 Simpson 积分
  - Richardson 外推

### Task C（23分，L1/L2）误差验证与图形分析

文件：`lab1_core/tests/test_core.py`、`lab1_core/notebook_core.ipynb`

- 验证中心差分精度优于前差/后差（同步长）。
- 验证 Simpson 在相同网格下显著优于梯形公式。
- 验证 Richardson 外推可进一步降低误差。
- 生成误差-步长图并解释“先降后升”的最优步长现象。

---

## 4. Lab2-Bonus（课后，30 分）

文件：`lab2_bonus/src/advanced_model.py`

主题：Debye 热容积分

- 使用 Gauss-Legendre 积分计算 Debye 热容中的积分项。
- 检查低温 `C_V ~ T^3` 与高温趋于常数极限（Dulong-Petit 趋势）。
- 比较梯形/Simpson/Gauss 方法在同精度目标下的采样点开销。

---

## 5. 自动测试与运行

```bash
pip install -r requirements.txt
python -m unittest discover -s lab1_core/tests -p "test_*.py" -v
python -m unittest discover -s lab2_bonus/tests -p "test_*.py" -v
```

---

## 6. 提交规范

- 禁止修改测试文件和 workflow。
- 必须提交 `Report_Template.md` 对应分析内容。
- 每段 AI 生成代码都要有 Prompt 记录与人工审查结论。
