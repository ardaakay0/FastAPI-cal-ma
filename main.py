from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []

# Add task to the DB (list in this case)
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task 

# Get all of the tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

# Get task by using task id. Raise exception if task id doesn't exist
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update task's elements by using task_id. Raise exception if task id doesn't exist
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    for ind, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[ind] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete task from the list by using task_id. Raise exception if task id doesn't exist
@app.delete("/tasks/{task_id}", response_model = Task)
def delete_task(task_id: UUID):
    for ind, task in enumerate(tasks):
        if task_id == task_id:
            return tasks.pop(ind)
    raise HTTPException(status_code = 404, detail="Task not found")

# Clears the list
@app.put("/tasks/delete_all/", response_model=List)
def clear_list():
    tasks = []
    return tasks

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0",port=8000)