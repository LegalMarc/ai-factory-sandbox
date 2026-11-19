#ifndef RINGBUF_H
#define RINGBUF_H

#include <stddef.h>

struct ringbuf {
    int *storage;
    size_t capacity;
    size_t head;
    size_t count;
};

void rb_init(struct ringbuf *rb, int *storage, size_t capacity);
int rb_push(struct ringbuf *rb, int value);
int rb_pop(struct ringbuf *rb, int *out);
size_t rb_len(const struct ringbuf *rb);

#endif
