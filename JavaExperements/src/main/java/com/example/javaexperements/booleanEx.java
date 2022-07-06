package com.example.javaexperements;

public class booleanEx {
    public static void main(String[] args) {
        boolean a = false;
        boolean b = false;
        boolean c = false;
        boolean d = false;
        System.out.println(((!a) & (!b) & c & d) ^ (a & b & (!c) & (!d)) ^ (a & (!b) & (!c) & d) ^ ((!a) & b & c & (!d)) ^ (a & (!b) & c & (!d)) ^ ((!a) & b & (!c) & d));
    }
    public static boolean booleanExpression(boolean a, boolean b, boolean c, boolean d) {
        return ((a != b) && (c != d)) || ((a != c) && (b != d));
    }
}
