#include "ringbuf.h"

void rb_init(struct ringbuf *rb, int *storage, size_t capacity) {
    rb->storage = storage;
    rb->capacity = capacity;
    rb->head = 0;
    rb->tail = 0;
    rb->len = 0;
}

int rb_push(struct ringbuf *rb, int value) {
    if (rb->len >= rb->capacity) {
        return -1;
    }
    rb->storage[rb->tail] = value;
    rb->tail = (rb->tail + 1) % rb->capacity;
    rb->len++;
    return 0;
}

int rb_pop(struct ringbuf *rb, int *out) {
    if (rb->len == 0) {
        return -1;
    }
    *out = rb->storage[rb->head];
    rb->head = (rb->head + 1) % rb->capacity;
    rb->len--;
    return 0;
}

size_t rb_len(const struct ringbuf *rb) {
    return rb->len;
}
