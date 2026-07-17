# # main.py
# from agent import root_agent
# from .retry_utils import run_agent_with_retry

# def generate_test_plan(owner, repo, file_path):
#     """
#     Constructs the prompt and calls the agent.
#     """
#     # 1. Create a dynamic prompt using f-strings
#     prompt = f"Please generate a comprehensive test plan for the file '{file_path}' in the repository '{owner}/{repo}'."
    
#     print(f"Asking agent to analyze {owner}/{repo}/{file_path}...")
    
#     try:
#         # 2. Call the agent using your retry wrapper
#         response = run_agent_with_retry(root_agent, prompt)
#         return response
#     except Exception as e:
#         return f"Error generating test plan: {e}"

# # 3. Run it directly
# if __name__ == "__main__":
#     # Example: Let's test the 'requests' library on GitHub
#     test_plan = generate_test_plan(
#         owner="psf", 
#         repo="requests", 
#         file_path="src/requests/api.py"
#     )
    
#     print("\n" + "="*40)
#     print("TEST PLAN GENERATED:")
#     print("="*40 + "\n")
#     print(test_plan)