# Day 63 - Terraform Variables

Variables in Terraform are quite important, as you need to hold values of names of instance, configs, etc.

We can create a `variables.tf` file which will hold all the variables.

```sh
variable "filename" {
default = "path/to/file/demo-var.txt"
}
```

```sh
variable "content" {
default = "This is coming from a variable which was updated"
}
```

These variables can be accessed by var object in `main.tf`

## Task-01

- Create a local file using Terraform

Hint:

```sh
resource "local_file" "devops" {
filename = var.filename
content = var.content
}
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3e707ff9-9e16-4849-bd7b-fb1140415133)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d42be9d6-bf58-40e9-8d3e-101e81001848)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/45c7afe6-beda-4db0-84aa-a896b580974c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1f2d2707-b77c-4ef9-8fcd-fb48e1feab83)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ced41db9-1cef-4b85-91bf-7daeb7407b8b)

![cghvjh](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2e9df2a7-def2-4d9f-84b0-ae849a2a1635)

## Data Types in Terraform

## Map

In Terraform, the map type is used to represent a collection of key-value pairs. It allows you to store and manipulate data in a structured way. A map is similar to a dictionary or hash table in other programming languages.

Here's an example of defining a map variable in Terraform:

```sh
variable "file_contents" {
type = map
default = {
"statement1" = "this is cool"
"statement2" = "this is cooler"
}
}
```

## Task-02 

- Use terraform to demonstrate usage of List, Set and Object datatypes
- Put proper screenshots of the outputs


Use `terraform refresh`

To refresh the state by your configuration file, reloads the variables




# Video Course

I can imagine, Terraform can be tricky, so best to use a Free video Course for terraform [here](https://bit.ly/tws-terraform)

Happy Learning :)
