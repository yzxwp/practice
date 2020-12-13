export var name = "yzxing";
export let age = "26";

export function person(name, age) {
    this.name = name;
    this.age = age;
    return `${this.name} ++++ ${this.age}`
}
