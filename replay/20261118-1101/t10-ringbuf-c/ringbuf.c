#include "ringbuf.h"

void rb_init(struct ringbuf *rb, int *storage, size_t capacity)
{
    rb->storage = storage;
    rb->capacity = capacity;
    rb->head = 0;
    rb->count = 0;
}

int rb_push(struct ringbuf *rb, int value)
{
    size_t index;

    if (rb->count == rb->capacity) {
        return -1;
    }

    index = (rb->head + rb->count) % rb->capacity;
    rb->storage[index] = value;
    rb->count++;
    return 0;
}

int rb_pop(struct ringbuf *rb, int *out)
{
    if (rb->count == 0) {
        return -1;
    }

    *out = rb->storage[rb->head];
    rb->head = (rb->head + 1) % rb->capacity;
    rb->count--;
    return 0;
}

size_t rb_len(const struct ringbuf *rb)
{
    return rb->count;
}
